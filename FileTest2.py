# Python code to create a file
fileO = open('TestPy2.txt','w')
fileO.write("This is the write command \n")
fileO.write("It allows us to write in a particular file")
fileO.close()

#fileR = open("TestPy2.txt", "r")
#print (fileR.read())

# Python code to illustrate append() mode
file = open('TestPy2.txt', 'a')
file.write("\nThis will add this line")
file.close()

fileR = open("TestPy2.txt", "r")
print (fileR.read())