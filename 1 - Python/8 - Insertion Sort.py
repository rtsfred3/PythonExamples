def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i-1
        while j >=0 and arr[j] > value:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = value
    return arr

def main():
    x = insertion_sort([2,7,3,6,10,11,1,4,5])
    print(x)
    return 0

main()