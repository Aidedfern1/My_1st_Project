""""
Elaborar un script de Python que reciba como argumentos:
arg0 = Ubicacion de un archivo.
arg1 = Comando a ejecutar; "--read, --pattern [pattern]"
read: Imprime linea a linea todo el archivo
pattern[pattern]: Busca [pattern] en el archivo e imprime todas lineas que cumplan con este patron.

Realizar la implementacion usando objetos como  clase, loops y listas
"""
""""
file = open('TestPy.txt','r')

for each in file:
    print(each)
"""

""""   
import argparse

parser= argparse.ArgumentParser(description="Script to read a file")

parser.add_argument("file",type= str, help="name the file you want to read")
parser.add_argument("-r","--read", dest="lecture",help= "read the located file")

args= parser.parse_args()

print(args.file)

file = open(args.file,'r')

for line in file:
    if "allow" in line:
        print(line)
"""
        

class LookPattern:
    def __init__(self, file:str , pattern:str):
        self.file= file
        self.pattern= pattern

    def read(self):
        self.Rfile = open(self.file,'r')

    def show(self):
        for line in self.Rfile:
            if "allow" in line:
                print(line)

L = LookPattern("TestPy2.txt","allow")

L.read()
print(L.show())