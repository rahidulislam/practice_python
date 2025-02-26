def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [1,2,3,4,5,6,7,8,9,10]
target = 9
index = linear_search(arr,target)
if index == -1:
    print("Element not found")
else:
    print(f"Element found at index {index}")