"""
with open("TestPy2.txt","r") as archivo:
    lineas= archivo.readlines()
    print(lineas)

for l in lineas:
    print(l.replace("\n",""))
"""

"""
with open("TestPy2.txt","r") as archivo:
    contenido= archivo.read()
    lineas= contenido.split("\n")
    print(lineas)
"""

with open("TestPy2.txt","r") as archivo:
    pos= archivo.seek(7)
    print(pos)
    contenido= archivo.read()
    lineas= contenido.split("\n")
    print(lineas)

with open("TestPy3.txt","w") as archivo:
    archivo.write("Jose\nAngel\nPino")

with open("TestPy3.txt","r") as lectura:
    print(lectura.read())