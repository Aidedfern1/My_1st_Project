class Burger:
    def __init__(self,size,tomato,lettuce,cheese,seasoning):
        self.size= size
        self.tomato= tomato
        self.lettuce= lettuce
        self.cheese= cheese
        self.seasoning = seasoning
    
    def showOrder(self):
        print("You ordered a "+ self.size + " size burger with " + self.tomato, self.lettuce, self.cheese + " and "+ self.seasoning)

order= Burger("Big", "no tomato", "lettuce", "cheese","ketchup")
order.showOrder()

print(order.lettuce,order.cheese)

