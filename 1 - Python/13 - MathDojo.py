class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num1, *nums):
        self.result += num1+sum(nums)
        return self
    
    def subtract(self, num1, *nums):
        self.result -= num1+sum(nums)
        return self

def main():
    print('==MathDojo==')
    md = MathDojo()
    
    print('=Add 2=')
    print(md.add(2).result)
    
    print('\n=Add 2, 5, 1=')
    print(md.add(2,5,1).result)
    
    print('\n=Subtract 3, 2=')
    print(md.subtract(3,2).result)
    return 0

main()