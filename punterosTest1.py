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

def CircleArea(r:float) -> float:
  area=m.pi*(r**2)

  return area

fun()
r= 4
ans=CircleArea(r)
print("The area of your circle is {}".format(ans))
