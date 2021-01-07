def selection_sort(arr):
    i, j, m = 0, 0, 0
    while i < len(arr):
        j, m = i, i
        while j < len(arr):
            if arr[j] < arr[m]:
                m = j
            j+=1
        arr[i], arr[m] = arr[m], arr[i]
        i+=1
    return arr

def main():
    x = selection_sort([2,7,3,6,10,11,1,4,5])
    print(x)
    return 0

main()