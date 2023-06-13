def removeduplicate(arr):
    new_list=[]
    for i in arr:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

my_list=[1,1,2,2,3]
removeduplicate(my_list)