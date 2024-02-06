survived=[]
names=[]
sex=[]
age=[]
male=[]
female=[]
others=[]
children=[]
childrenSurvived = 0
f1=open("titanic.csv","r")
f1.readline()
list1=f1.readlines()
len1=len(list1)
for i in range(0,len1,1):
    info1=list1[i]
    list2=info1.split(",")
    survived.append(int(list2[1]))
    names.append(list2[4])
    sex.append(list2[5])
    if list2[6] == "":
        age.append(40)
    else:
        age.append(int(float(list2[6])))

total_survived=sum(survived)
total_deceased=len1-total_survived
for i in range(0,len1,1):
    if sex[i]=="male":
        male.append(names[i])
    elif sex[i]=="female":
        female.append(names[i])
    else:
        others.append(names[i])
for i in range(0,len1,1):
    if age[i] < 10:
        children.append(names[i])
print("The total number of people who survived:",total_survived)
print("The total number of people who survived:",total_deceased)

total_male=len(male)
total_female=len(female)
total_others=len(others)
total_children=len(children)
print("The total number of males:",total_male,)
print("The total number of females:",total_female)
print("The total number of other genders:",total_others)
print("The total number of children:",total_children)

for i in range(0,len1,1):
    if age[i] < 10 and survived[i] == 1:
        childrenSurvived = childrenSurvived + 1
    else:
        childrenSurvived = childrenSurvived
print(childrenSurvived)

 

