def leftrotate(arr,n,k):
    if n==1:
        print(arr)
    else:
        new=[]
        for i in range(k%n,n):
            new.append(arr[i])
        for i in range(0,k%n):
            new.append(arr[i])
        print(new)

arr=[1,2,3,4,5,6,7]
n=len(arr)
leftrotate(arr,n,3)