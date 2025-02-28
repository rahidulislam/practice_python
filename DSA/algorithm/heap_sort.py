def heapfy(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[left]>arr[largest]:
        largest = left
    
    if right<n and arr[right]>arr[largest]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapfy(arr,n,largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n//2-1,-1,-1):
        heapfy(arr,n,i)

    # Swap the root element with the last element and heapify the root element
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapfy(arr,i,0)

# arr = [38, 27, 43, 3, 9, 82, 10]
arr = [4,10,3,5,1]
heap_sort(arr)
print("Sorted array is:",arr)