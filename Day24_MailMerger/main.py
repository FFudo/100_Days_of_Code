#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Day24_MailMerger/Input/Names/invited_names.txt", "r") as f:
    names = f.read().splitlines()

with open ("./Day24_MailMerger/Input/Letters/starting_letter.txt", "r") as f:
    start_letter = f.read()

for name in names:
    new_letter = start_letter.replace("[name]", name)
    with open(f"./Day24_MailMerger/Output/{name}_letter.txt", "w") as f:
        f.write(new_letter)
    

