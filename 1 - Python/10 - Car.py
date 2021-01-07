class car:
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.miles = milage
        self.tax = 0.12
        if self.price > 10000:
            self.tax = 0.15
    
    def display_all(self):
        print('Price:', self.price)
        print('Speed:', self.speed)
        print('Milage:', self.miles)
        print('Tax:', self.tax)

def main():
    print('==Example 1==')
    c1 = car(2000, "35mph", "Full", "15mpg")
    c1.display_all()
    
    print('\n==Example 2==')
    c1 = car(2000, "5mph", "Not Full", "105mpg")
    c1.display_all()
    
    print('\n==Example 3==')
    c1 = car(2000, "15mph", "Kind of Full", "95mpg")
    c1.display_all()
    
    print('\n==Example 4==')
    c1 = car(20000000, "35mph", "Empty", "15mpg")
    c1.display_all()
    return 0

main()