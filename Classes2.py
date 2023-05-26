class Bottle:
    def __init__(self,volume: int,type_:str):
        self.volume = volume
        self.type_ = type_

    def pour(self):
        print("Pouring...")

    def fill(self):
        print("Filling...")   

    def recycle(self):
        print("Recycling")

Agua = Bottle(500,"pet")

print(Agua.volume)
print(Agua.type_)

Agua.fill()
Agua.pour()
Agua.recycle()