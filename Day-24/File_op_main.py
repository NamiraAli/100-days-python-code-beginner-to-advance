#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt") as file:  # ./ means go to current 1 st folder here it goes to Mail Merge Project start folder then we go to input then in it is letters then  txt file
    newl=file.read()
    print(newl)

with open("./Input/Names/invited_names.txt") as filenames:
    filenames=filenames.readlines()
    print(filenames)

for x in filenames:
    clean_name = x.strip() #strip is used to remove extra spaces and new line
    #here we use strip because in file name creation we cannot use spaces for file name
    letter=newl.replace("[name]",x)

    with open(f"./Output/{clean_name}"+"_invitation" ,"w") as new_file_name:
        new_file_name.write(letter)


