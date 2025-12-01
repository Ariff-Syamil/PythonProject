#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


invite = open("./Input/Names/invited_names.txt")
names = invite.readlines()
invite.close()
# print(names)
for name in names:
    invited = name.strip()
    # print(invited)
    with open("./Input/Letters/testing.txt") as file:
      starting = file.read()
      letter = starting.replace("[name]", f"{invited}")
      # print(letter)
      # pdf and docx file is corrupted when created.
      # use only txt file
      with open(f"./Output/ReadyToSend/letter_for_{invited}.txt", "w") as writing_letter:
          writing_letter.write(letter)