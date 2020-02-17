#bubble sort
arr = list(map(int,input().split()))
sorted_arr = sorted(arr)
print(arr)

sorted_arr1 = []

for k in range(len(arr)-1):
    for i in range(len(arr)-k-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

print(arr)
print(sorted_arr)