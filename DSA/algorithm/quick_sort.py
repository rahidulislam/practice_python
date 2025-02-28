def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x<pivot]
        middle = [x for x in arr if x==pivot]
        right = [x for x in arr if x>pivot]
        return quick_sort(left) + middle + quick_sort(right)
# arr = [5, 2, 9, 1, 5, 6]
arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array is:",quick_sort(arr))