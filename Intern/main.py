from data_manager import Data_manager
import os
from configparser import ConfigParser
import sys


# ---------------------------------- Generate files -----------------------------------------
file = "config.ini"
configparser = ConfigParser()
configparser.read(file)

PATH = configparser['generated_files']['PATH']

HOST = configparser['database']['HOST']
USER = configparser['database']['USER']
PASSWORD = configparser['database']['PASSWORD']
CHARSET = configparser['database']['CHARSET']

data_manager = Data_manager(host=HOST, user=USER, password=PASSWORD, charset=CHARSET)


C_PERIMETRE = configparser['args']['C_PERIMETRE']
C_DOC = configparser['args']['C_DOC']
D_REPORTING = configparser['args']['D_REPORTING']
C_SUPERVISEUR = configparser['args']['C_SUPERVISEUR']


# C_PERIMETRE = os.environ['C_PERIMETRE']
C_PERIMETRE_list = "'" + C_PERIMETRE.replace(",", "','") + "'"
# C_DOC = os.environ['C_DOC']
C_DOC_list = "'" + C_DOC.replace(",", "','") + "'"
# D_REPORTING = os.environ['D_REPORTING']
# C_SUPERVISEUR = os.environ['C_SUPERVISEUR']

# C_PERIMETRE = sys.argv[1]
# C_PERIMETRE_list = "'" + C_PERIMETRE.replace(",", "','") + "'"
# C_DOC = sys.argv[2]
# C_DOC_list = "'" + C_DOC.replace(",", "','") + "'"
# D_REPORTING = sys.argv[3]
# C_SUPERVISEUR = sys.argv[4]


# filter db data
sql = f"SELECT * FROM corep_data_v2 WHERE D_REPORTING='{D_REPORTING}' " \
      f"and ('{C_PERIMETRE}'='*' or C_PERIMETRE in ({C_PERIMETRE_list})) " \
      f"and ('{C_DOC}'='*' or C_DOC in ({C_DOC_list})) " \
      f"order by C_PERIMETRE, C_DOC, C_ONGLET, C_LIGNE;"
# bring data
df = data_manager.get_db_data(db='corep_db', query=sql)
# bring templates
templates = data_manager.get_templates(database="corep_db", c_superviseur=C_SUPERVISEUR, d_reporting=D_REPORTING)

data_manager.generate_workbooks(dataframe=df, templates=templates, out_directory=PATH)


# ---------------------------------- store and get files -----------------------------------------
# # assign directory
# data_manager = Data_manager()
# directory = 'templates'
# data_manager.insert_directory_files(directory=directory, db='corep_db')
#
#
# # get a file from db
# data_manager.get_file(db='corep_db', d_reporting='2022-03-31', c_superviseur='ABE_V3.0', c_doc='CR SA.xlsx',
#                       directory='recovered_templates')
