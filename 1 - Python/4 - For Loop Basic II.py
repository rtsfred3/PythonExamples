def makeItBig(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "Big"
    return arr

def countPositives(arr):
    count = 0
    for i in arr:
        if i > 0:
            count+=1
    arr[-1] = count
    return arr

def sumTotal(arr):
    total = 0
    for i in arr:
        total+=i
    return total

def multiples(arr):
    total = 0
    for i in arr:
        total+=i
    return total/len(arr)

def minimum(arr):
    minVal = arr[0]
    for i in range(len(arr)):
        if minVal > arr[i]:
            minVal = arr[i]
    return minVal

def maximum(arr):
    maxVal = arr[0]
    for i in range(len(arr)):
        if maxVal < arr[i]:
            maxVal = arr[i]
    return maxVal

def analyze(arr):
    total, minVal, maxVal = 0, arr[0], arr[0]
    for i in range(len(arr)):
        if maxVal < arr[i]:
            maxVal = arr[i]
        else:
            minVal = arr[i]
        total+=arr[i]
    return {'total':total, 'avg':total/len(arr), 'min':minVal, 'max':maxVal, 'length':len(arr)}

def reverse(arr):
    newArr = []
    i = len(arr)-1
    while i>=0:
        newArr.append(arr[i])
        i-=1
    return newArr

def main():
    print("==Biggie Size==")
    print(makeItBig([-1, 3, 5, -5]))
    
    print("==Count Positives==")
    print(countPositives([-1, 1, 1, 1]))
    
    print("==SumTotal==")
    print(sumTotal([1,2,3,4]))
    
    print("==Average==")
    print(multiples([1,2,3,4]))
    
    print("==Minimum==")
    print(minimum([1,2,3,4]))
    
    print("==Maximum==")
    print(maximum([1,2,3,4]))
    
    print("==UltimateAnalyze==")
    print(analyze([1,2,3,7,4]))
    
    print("==ReverseList==")
    print(reverse([1,2,3,4]))

main()