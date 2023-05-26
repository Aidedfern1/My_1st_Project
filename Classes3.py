class Carro:
    def __init__(self,marca, modelo ):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print("El",self.marca,self.modelo,"se ha arrancado")
    
    def parar(self):
        self.arrancado = False
        print("El",self.marca,self.modelo, "se ha parado") 

laguna = Carro("Renault","Laguna")
Tesla = Carro("Tesla","Modelo 3")  

print(type(laguna))
print(type(Tesla))

print(laguna.marca, laguna.modelo)
print(Tesla.marca, Tesla.modelo)

laguna.arrancar()
Tesla.arrancar()

print(laguna.arrancado)
print(Tesla.arrancado)

laguna.parar()
Tesla.parar()

print(laguna.arrancado)
print(Tesla.arrancado)