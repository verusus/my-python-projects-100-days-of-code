import pymysql.cursors
import pymysql
import pandas as pd
from openpyxl import load_workbook
from pathlib import Path
from io import BytesIO
from configparser import ConfigParser

# file = "config.ini"
# configparser = ConfigParser()
# configparser.read(file)

# HOST = configparser['database']['HOST']
# USER = configparser['database']['USER']
# PASSWORD = configparser['database']['PASSWORD']
# CHARSET = configparser['database']['CHARSET']

class Data_manager:

    def __init__(self, host, user, password, charset):
        self.HOST = host
        self.USER = user
        self.PASSWORD = password
        self.CHARSET = charset

    def make_connection_with_db(self, db):
        """Returns the connection object of a specified db."""
        connection = pymysql.connect(host=self.HOST,
                                     user=self.USER,
                                     password=self.PASSWORD,
                                     db=db,
                                     charset=self.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def get_db_data(self, db, query):
        """Returns the query's data from the specified db as a dataframe."""
        # Connect to the database
        connection = self.make_connection_with_db(db)

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()
                df = pd.DataFrame(data)
        finally:
            connection.close()
            return df

    def save_doc(self, workbook, current_doc, current_perimetre, directory):
        """Removes the reference sheet (the first sheet) and saves the document in the specified directory."""
        # delete first sheet
        workbook.remove(workbook.active)
        # give doc title C_DOC and save
        workbook.save(filename=f"{directory}/{current_doc}-{current_perimetre}.xlsx")

    def is_doc_changed(self, current_perimetre, row_perimetre, current_doc, row_doc):
        """returns True if the document is changed."""
        if current_perimetre != row_perimetre or current_doc != row_doc:
            return True
        else:
            return False

    def generate_workbooks(self, dataframe: pd.DataFrame, templates, out_directory):
        """Generates workbooks to the out_directory folder using the templates. it uses the passed DataFrame to fill
        the output workbooks. """
        workbook = None
        current_perimetre = None
        current_doc = None

        for index, row in dataframe.iterrows():
            # si le perimetre ou c_doc a été changé: sauvegarder le fichier actuel(current_perimetre != None)
            # et crèer le nouveau fichier
            if self.is_doc_changed(current_perimetre, row['C_PERIMETRE'], current_doc, row['C_DOC']):
                if current_perimetre is not None and current_doc is not None:
                    self.save_doc(workbook=workbook, current_doc=current_doc, current_perimetre=current_perimetre,
                                  directory=out_directory)
                # load template
                workbook = templates[row["C_DOC"]]    # we retreive the workbook we constructed in the dictionary

                current_perimetre = row['C_PERIMETRE']
                current_doc = row['C_DOC']
                # initializing current_sheet everytime we create new doc
                current_sheet = None

            # if current sheet changed or new doc has created: make another copy of the reference sheet first,
            # else continue filling its cells.
            if current_sheet != row['C_ONGLET']:
                current_sheet = row['C_ONGLET']
                ws_copy = workbook.copy_worksheet(workbook.active)
                # give title L_ONGLET
                ws_copy.title = row['L_ONGLET']
                # set cell amount of this iteration
                cell_id = row['C_COLONNE'] + str(row['NO_EXCEL'])
                ws_copy[cell_id] = row['MONTANT']
            else:
                # set cell amount of current iteration
                cell_id = row['C_COLONNE'] + str(row['NO_EXCEL'])
                ws_copy[cell_id] = row['MONTANT']

        if current_perimetre is not None and current_doc is not None:
            self.save_doc(workbook=workbook, current_doc=current_doc, current_perimetre=current_perimetre,
                          directory=out_directory)

    def get_templates(self, database, d_reporting, c_superviseur):
        """Returns all files from the specified database as a dictionary with each key is "c_doc" & its value is a
        template workbook. """
        query = f"""SELECT * FROM corep_db.reg_ref_etat_corep WHERE d_reporting='{d_reporting}' 
        AND c_superviseur='{c_superviseur}'"""

        connection = self.make_connection_with_db(database)
        with connection.cursor() as cursor:
            cursor.execute(query)
            list_of_dict_data = cursor.fetchall()

        templates = {record['c_doc']: load_workbook(BytesIO(record['content'])) for record in list_of_dict_data}
        return templates

    def file_to_binary(self, filename):
        """Converts a file to binary format."""
        with open(filename, 'rb') as file:
            binary_data = file.read()
        return binary_data

    def insert_directory_files(self, directory, db):
        """It loops on the directory files and inserts all the files into the db with this schema:
        d_reporting(YYYY-MM-DD), c_superviseur, c_doc, content(file with size<16MB)."""
        # make connection with db
        connection = self.make_connection_with_db(db)

        # iterate over files in
        # that directory
        files = Path(directory).glob('*')
        for file in files:
            query = f"""INSERT INTO corep_db.reg_ref_etat_corep (d_reporting, c_superviseur, c_doc, content)
                     VALUES ('2022-03-31', 'ABE_V3.0', '{file.name.split('.')[0]}', %s);"""
            values = (self.file_to_binary(file))
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

    def binary_to_file(self, binary_data, filename):
        """Turns a stream of Bytes into a file."""
        with open(filename, 'wb') as file:  # if the file doesn't exist, it creates it
            wb = file.write(binary_data)
        return wb


