# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# take invited names list
with open("Input/Names/invited_names.txt", "r") as names_file:
    names_list = names_file.readlines()

# looping on each name in the invited list
for name in names_list:
    # cut the extra \n from each line
    name = name.strip("\n")
    # reading the email sample each time
    with open("Input/Letters/starting_letter.txt", mode="r") as file:
        fileData = file.read()
    fileData = fileData.replace('[name]', name)
    # Save the letter in the folder "ReadyToSend".
    with open(f"Output/ReadyToSend/letter_to_send_to_{name}.txt", "w") as file:
        file.write(fileData)





