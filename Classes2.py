class Bottle:
    def __init__(self,volume: int,type_:str, color: str):
        self.volume = volume
        self.type_ = type_
        self.color = color

    def pour(self):
        print("Pouring...")

    def fill(self):
        print("Filling...")   

    def recycle(self):
        print("Recycling")

Agua = Bottle(500,"pet", "white")

print(Agua.volume)
print(Agua.type_)
print(Agua.color)

Agua.fill()
Agua.pour()
Agua.recycle()