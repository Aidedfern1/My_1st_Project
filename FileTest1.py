# a file named "TestPy", will be opened with the reading mode.
file = open('TestPy.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)

# Python code to illustrate read() mode
file = open("TestPy.txt", "r")
print (file.read(12))