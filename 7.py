def shuffle1(listA):
    import random
    list1 = listA
    list2 = []
    len1 = len(list1)
    for i in range(0,len1,1):
        len1 = len(list1)
        rand1 = random.randint(0,len1-1)
        list2.append(list1[rand1])
        list1.remove(list1[rand1])
    return list2
        
list1 = [2,4,6,8,10,12,14,16,18]
list2 = shuffle1(list1)
print(list2)
