def leftrotate(arr,n,k):
    if n==1:
        print(arr)
    else:
        new=[]
        for i in range(n-k,n):
            new.append(arr[i])
        for i in range(0,n-k):
            new.append(arr[i])
        print(new)

arr=[-1,-100,3,99]
n=len(arr)
leftrotate(arr,n,2)