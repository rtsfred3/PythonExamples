def basic():
    for i in range(151):
        print(i)

def multiplesOfFive():
    for i in range(5, 1000000, 5):
        print(i)

def codingDojoWay():
    for i in range(1, 101):
        print(i)
        if i % 5:
            print("Coding", end="")
        if i % 10:
            print("Dojo")

def sumOdds():
    print(sum([i for i in range(500000) if i % 2 == 1]))
    
def byFours():
    i = 2018
    while i > 0:
        print(i)
        i-=4
        
def flexCount(lowNum, highNum, mult):
    i = lowNum
    while i <= highNum:
        if i % mult == 0:
            print(i)
        i+=1

def main():
    print("==Basic==")
    basic()
    
    print("==Multiples of Five==")
    multiplesOfFive()
    
    print("==Counting, the Dojo Way==")
    codingDojoWay()
    
    print("==Whoa. That Sucker's Huge==")
    sumOdds()
    
    print("==Countdown by Fours==")
    byFours()
    
    print("==Flexible Countdown==")
    flexCount(2, 9, 4)    

main()