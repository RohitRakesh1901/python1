def quiz2(topic2,str2):
    topic1 = topic2
    str1 = str2
    def quiz1(topic1):
        import random
        fname1 = "Quiz - "
        fname2 = topic1
        fname3 = ".csv"
        f1 = open(fname1+fname2+fname3,"r")
        f1.readline()
        list1 = f1.readlines()
        random.shuffle(list1)
        len1 = len(list1)
        marks = []
        wrong = []
        countries = []
        capitals = []

        for i in range(0,len1,1):
            list2 = list1[i].split(",")
            countries.append(list2[0])
            capitals.append(list2[1].replace("\n",""))

        for i in range(0,10,1):
            response1 = input(str1+str(countries[i]+"?"))
            if response1 == capitals[i]:
                marks.append(10)
            else:
                marks.append(0)
                wrong.append(i)

        total = (sum(marks))
        len2 = len(wrong)
        return(total,wrong,countries,capitals)
    result = quiz1(topic1)
    total1 = (result[0])
    wrong1 = (result[1])
    column1 = (result[2])
    column2 = (result[3])
    print("You have scored marks of ",total1)
    for i in range(0,len(wrong1),1):
        print(column1[wrong1[i]],column2[wrong1[i]])
#quiz2("Capitals","What is the capital of ")
quiz2("Currency","What is the currency of ")
