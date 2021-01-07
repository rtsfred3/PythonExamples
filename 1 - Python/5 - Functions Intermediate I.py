import random

# Create beCheerful().  Within it, print string "good morning!" 98 times.
def beCheerful(repeat=1):
    x = "good morning!\n"*repeat
    print("*"*80)
    print(x.strip())

def randInt(minVal=0, maxVal=100):
    return int((random.random()*((maxVal+1)-minVal))+minVal)

def main():
    beCheerful(98)
    arr = [randInt(5, 10) for i in range(100)]
    print("Min:", min(arr))
    print("Max:", max(arr))

main()