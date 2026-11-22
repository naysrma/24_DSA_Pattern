def removeDuplicates(arr):
    if len(arr) == 0:
        return 0

    j = 1
    for i in range(1, len(arr)):
        if(arr[i] != arr[j - 1]):
            arr[j] = arr[i]
            j += 1

    return j


arr = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(arr))