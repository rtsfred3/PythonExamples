class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print('Price:', self.price)
        print('Max Speed:', self.max_speed)
        print('Total Miles:', self.miles)
    
    def ride(self):
        print("Riding")
        self.miles+=10
        return self
    
    def reverse(self):
        print("Reversing")
        self.miles-=5
        return self

def main():
    print('==First Instance==')
    b1 = Bike(100, "40mph")
    b1.ride()
    b1.ride()
    b1.ride()
    b1.reverse()
    b1.displayInfo()
    
    print('==Second Instance==')
    b2 = Bike(100, "40mph")
    b2.ride()
    b2.ride()
    b2.reverse()
    b2.reverse()
    b2.displayInfo()
    
    print('==Third Instance==')
    b3 = Bike(100, "40mph")
    b3.reverse()
    b3.reverse()
    b3.reverse()
    b3.displayInfo()    
    return 0

main()