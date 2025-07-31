file = open('text.txt')

#read all
#print(file.read())

#read 2nd byte of txt file
#print(file.read(10))

#read line by line
#print(file.readline())
#print(file.readline())


#using while loop
#line = file.readline()
#while(line!=""):
#    print(line)
#    line = file.readline()


#for loop to put all lines into a list and iterate
#list = ["animals", "cat", "dog", "fly", "elephant"]
for line in file.readlines():
    print(line)


file.close()