class Person:
    """
    Provides some arithmetic functions
    """
    
    def __init__(self,age,weight,height,first_name,last_name,catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase= catch_phrase

    def walk(self):
        print("Walking...")

    def run(self):
        print("Running...")

user = Person(25,80,177,"Jon","Snow","You know nothing,Jon Snow")

print(user.catch_phrase)

user.walk()
user.run()