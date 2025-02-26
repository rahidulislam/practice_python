# Binary search is a fast search algorithm with run-time complexity of O(log n).
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [1,2,3,4,5,6,7,8,9,10]
target = 1
index = binary_search(arr,target)
if index == -1:
    print("Element not found")
else:
    print(f"Element {target} found at index {index}")

# Recursive binary search
def recursive_binary_search(arr, left, right, target):
    if left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_binary_search(arr,mid+1,right,target)
        else:
            return recursive_binary_search(arr,left,mid-1,target)
    return -1
arr = [1,2,3,4,5,6,7,8,9,10]
target = 10
index = recursive_binary_search(arr,0,len(arr)-1,target)
if index == -1:
    print("Element not found")
else:
    print(f"Element {target} found at index {index}")