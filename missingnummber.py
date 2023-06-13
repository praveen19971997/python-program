def missing(arr,n):
    sum=int((n*(n+1))/2)
    sum1=0
    for i in range(0,len(arr)):
        sum1=sum1+arr[i]
    print(sum-sum1)
arr=[1,3]
missing(arr,3)
    