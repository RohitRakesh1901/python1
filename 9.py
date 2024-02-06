f1 = open("Capitals.csv","r")
list1 = f1.readlines()
len1 = len(list1)
marks = []
wrong = []

countries = []
capitals = []
#print(len1)
for i in range(0,len1,1):
    
    list2 = list1[i].split(",")
    countries.append(list2[0])
    capitals.append(list2[1].replace("\n",""))

#print(countries)
#print(capitals)
for i in range(0,10,1):
    
    response1 = input("What is the capital of "+str(countries[i])+"?")
    if response1 == capitals[i]:
        marks.append(10)
    else:
        marks.append(0)
        wrong.append(i)

print(wrong)
print(sum(marks))
len2 = len(wrong)
for i in range(0,len2,1):
    print(countries[wrong[i]],capitals[wrong[i]])
   
        

