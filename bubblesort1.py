def bubblesort(arr):
    print("Original Array: ")
    for i in arr:
        print(i, end=" ")
    print()
    n = len(arr)
    for i in range(n):
        print("Iteration: ", i)
        swapped = False
        for j in range(n-i-1): # last element is sorted
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap
                swapped = True
        for i in arr:
            print(i, end=" ")
        print()
        if not swapped:
            break

Arr = [9, 3, 6, 2, 1, 16, 6]
bubblesort(Arr)
print(" Sorted Array: ")
for i in Arr:
    print(i, end=" ")
  