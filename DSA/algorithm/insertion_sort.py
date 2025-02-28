# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key =arr[i]
#         j = i-1
#         print("Before while",j)
#         # print(arr[j],key)
#         while j >=0 and arr[j]>key:
#             arr[j+1] = arr[j]
#             j -=1
#             print("after while",j)
#         arr[j+1] = key

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -=1
arr = [5, 2, 9, 1, 5, 6]
insertion_sort(arr)
print("Sorted array is:",arr)