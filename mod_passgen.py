def passgen2(size,count):
    def passgen1(size):
        import random
        list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        list2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        list3 = [0,1,2,3,4,5,6,7,8,9]
        list4 = list1+list2+list3
        len1 = len(list1)
        len2 = len(list2)
        len3 = len(list3)
        len4 = len(list4)
        pwd4 = ""


        rand1 = random.randint(0,len1-1)
        pwd1 = list1[rand1]

        rand2 = random.randint(0,len2-1)
        pwd2 = list2[rand2]

        rand3 = random.randint(0,len3-1)
        pwd3 = list3[rand3]

        for i in range(0,size-3,1):    
            rand4 = random.randint(0,len4-1)
            pwd4 = pwd4+str(list4[rand4])

        pwd = pwd1 + pwd2 + str(pwd3) + str(pwd4)

        print(pwd)

    for i in range(0,count,1):
        passgen1(size)

