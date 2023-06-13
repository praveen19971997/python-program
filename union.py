def union(arr1,arr2):
    temp=[]
    for i in range(0,len(arr1)):
        temp.append(arr1[i])
    for i in range(0,len(arr2)):
        if arr2[i] not in temp:
            temp.append(arr2[i])
    print(temp)

arr1=[1,2,3,4,5,6,7,8,9,10]
arr2=[2,3,4,4,5,11,12]
union(arr1,arr2)