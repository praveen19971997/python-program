def consecutive(arr):
    count=0
    for i in range(0,len(arr)):
        count=count+1
        if arr[i]==0:
            count=0
    print(count)

arr=[1,0,1,1,0,1]
consecutive(arr)