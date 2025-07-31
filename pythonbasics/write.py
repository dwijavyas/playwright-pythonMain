#read the file put them in list
#reverse the list
#write the reversed list back to file


#this will open and close file
with open('text.txt', 'r') as reader:
    content = reader.readlines() #puts into a list
    reversed(content) #reverses the list
    with open('text.txt', 'w') as writer:
        for line in  reversed(content):
            writer.write(line)
