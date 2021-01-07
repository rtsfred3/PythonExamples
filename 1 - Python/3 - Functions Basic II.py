def coutdown(val):
    arr = []
    while val>=0:
        arr.append(val)
        val-=1
    return arr

def printReturn(arr):
    print(arr[0])
    return arr[1]

def firstPlusLength(arr):
    return arr[0]+len(arr)

def largerThanSecond(arr):
    if len(arr) <= 1: return False
    newArr = []
    for i in arr:
        if i > arr[1]:
            newArr.append(i)
    return newArr

def thisThatValues(num1, num2):
    if num1 == num2: print("Jinx!")
    arr = []
    for i in range(num1):
        arr.append(num2)
    return arr

def main():
    print('==Countdown==')
    print(coutdown(5))
    
    print('==Print and Return==')
    print(printReturn([5, 2]))
    
    print('==First Plus Length==')
    print(firstPlusLength([5, 2]))
    
    print('==Values Greater than Second==')
    print(largerThanSecond([5, 4, 6, 1, 3]))
    
    print('==This Length, That Value==')
    print(thisThatValues(3, 3))    


main()