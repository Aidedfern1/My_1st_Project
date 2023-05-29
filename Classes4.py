class Company:
    def __init__(self, name:str, company: str, city:str):
        self.name = name
        self.company = company
        self.city = city
 
    def show(self):
        print("Hello my name is " + self.name+" and I" +
              " work in "+self.company+" "+ self.city + "!")
 
 
obj = Company("Angel", "ZF", "Monterrey")
obj.show()

print(obj.name, obj.company, obj.city)