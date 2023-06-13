#check if array is sorted or not
def checksorted(arr,n):
    flag=1
    for i in range(0,n-1):
        if arr[i]>=arr[i+1]:
            flag=0
    return flag
my_list=[90,80,100,70,40,30]
ans=checksorted(my_list,5)
print(ans)
