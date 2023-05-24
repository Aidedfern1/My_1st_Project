a = 5
b = a
print("a = {}; b = {}".format(a,b)) # (1)
print(b is a) # resultado: True

a = 6
print("a = {}; b = {}".format(a,b)) # (2)
print(b is a) # resultado: False