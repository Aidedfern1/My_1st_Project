import math as m

a = 5
b = a
print("a = {}; b = {}".format(a,b)) # (1)
print(b is a) # resultado: True

a = 6
print("a = {}; b = {}".format(a,b)) # (2)
print(b is a) # resultado: False

numero = 1
otroNumero = 2
print(id(numero))
print(id(otroNumero))

def fun():
  print("Hello There!")

def CircleArea(r:float):
  area=m.pi*(r**2)

  return area

def SquareArea(L):
  areaS= L**2

  return areaS

fun()
r= 4
ans=CircleArea(r)
ans2= SquareArea(12)
print("The area of your circle is {}".format(ans))
print("The area of your square is {}".format(ans2))

val = input("Enter your value: \n")
print(val)
