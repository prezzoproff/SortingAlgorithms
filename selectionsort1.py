def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        swapped = True
        if not swapped:
            break

Arr = [3, 9, 8, 2, 20, 90, 3, 1, 0]
print("Original Array:")
for i in Arr:
    print(i, end=" ")
print()
print ("Sorted Array:") 
selection_sort(Arr) 
for i in Arr:
    print(i, end=" ")