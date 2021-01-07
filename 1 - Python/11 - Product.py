class product:
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        return round(self.price+self.price*tax, 2)
    
    def returned(self, reason):
        if reason == 'defective':
            self.status = reason
            self.price = 0
        elif reason == 'like_new':
            self.status = 'for_sale'
            #self.price = 0
        elif reason == 'opened':
            self.status = 'used'
            self.price = round(self.price*0.8, 2)
        return self
    
    def displayInfo(self):
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Price with tax:", self.add_tax(0.1))
        print("Weight:", self.weight)
        print("Status:", self.status)
        return self

def main():
    p1 = product(3.10, "Cereal", "100lbs", "Generic")
    print('==Inital Product Info==')
    p1.displayInfo()
    
    print('\n==Product Sold==')
    p1.sell().displayInfo()
    
    print('\n==Product Returned `like_new`==')
    p1.returned("like_new").displayInfo()
    
    print('\n==Product Returned `opened`==')
    p1.returned("opened").displayInfo()    
    
    print('\n==Product Returned `defective`==')
    p1.returned("defective").displayInfo()
    return 0

main()