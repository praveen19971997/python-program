def move(arr):
    for i in range(0,len(arr)):
        if arr[i]==0:
            arr.append(arr[i])
            arr.remove(arr[i])
    print(arr)

arr=[1,0,2,3,0,4,0,1]
move(arr)