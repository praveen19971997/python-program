def largest(arr,n):
    large=0
    second=0
    for i in range(0,n):
        if arr[i]>large:
            large=arr[i]
    print(large)

arr=[10,2,30,0,1]
largest(arr,5)