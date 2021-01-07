class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health-=1
        return self
    
    def run(self):
        self.health-=5
        return self
    
    def displayHealth(self):
        print(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 150)
    
    def pet(self):
        self.health+=5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name, 170)
    
    def fly(self):
        self.health-=10
        return self
    
    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")
        return self

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 135)

def main():
    print('==Animal==')
    animal = Animal("Spot", 15)
    animal.walk().walk().walk().run().run().displayHealth()
    
    print('\n==Dog==')
    dog = Dog("Spot")
    dog.walk().walk().walk().displayHealth().run().run().displayHealth().pet().displayHealth()
    try:
        dog.fly().displayHealth()
    except:
        print("This dog can't fly")
    
    print('\n==Dragon==')
    dragon = Dragon("Spot")
    dragon.displayHealth().fly().displayHealth()
    
    print('\n==Cat==')
    cat = Cat("Spot")
    cat.displayHealth()
    
    try:
        cat.fly().displayHealth()
    except:
        print("This cat can't fly")
    
    try:
        cat.pet().displayHealth()
    except:
        print("This cat be pet")    
    return 0

main()