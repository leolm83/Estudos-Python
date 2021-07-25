#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter=open("./Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r")
myletter=letter.readlines()
letter.close()
friends_name=open("./Mail Merge Project Start/Input/Names/invited_names.txt",mode="r")
friends=friends_name.readlines()
friends_name.close()

for name in friends:
    #print(name)
    name=name.replace("\n","")
    
    new_letter = open(f"./Mail Merge Project Start/Output/ReadyToSend/{name}_letter.txt", "a")
    #print(myletter)
    for index,line in enumerate(myletter):
        #print(line)
        if index==0:
            line=line.replace("[name]",name)
            new_letter.write(line)
        else:
            new_letter.write(line)
    new_letter.close()
friends_name.close()
