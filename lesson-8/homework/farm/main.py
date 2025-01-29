
class Animal:

    def __init__(self, name, age, weight):
        self.name = name 
        self.age = age 
        self.weight = weight

    def __str__(self):
        return f"Animal({self.name}, {self.age}, {self.weight})"

    def sleep(self):
        return f"{self.name} is sleeping!"
    
    def eat(self):
        return f"{self.name} is eating!"
    
    def run(self):
        return f"{self.name} is running"
    
    def sound(self):
        return f"{self.name} is making sound"




class Cow(Animal):
    def __init__(self, name, age, weight, milk):
        super().__init__(name, age, weight)
        self.milk_production = milk
    

    def __str__(self):
        return f"Animal Cow({self.name}, {self.age}, {self.weight})"
    
    def produce_milk(self):
        return f"{self.name} produces {self.milk} litres of milk per day."
    
    def sound(self):
        return f"{self.name} is saying 'mooo'"
    
    
class Chicken(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    

    def __str__(self):
        return f"Animal Chicken({self.name}, {self.age}, {self.weight})"

    def sound(self):
        return f"{self.name} is saying 'to-to-to'"


class Sheep(Animal):
    def __init__(self, name, age, weight, wool):
        super().__init__(name, age, weight)
        self.wool = wool

    def produce_wool(self):
        print(f"{self.name} produces {self.wool} kg of wool per year.")


    def __str__(self):
        return f"Animal Sheep({self.name}, {self.age}, {self.weight})"


    def sound(self):
        return f"{self.name} is saying 'baaa'"

