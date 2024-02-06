difflines = []
f1 = open("file1.txt","r")
f2 = open("file2.txt","r")
list1 = f1.readlines()
list2 = f2.readlines()
list3 = []
list4 = []
len1 = len(list1)
for i in range(0,len1,1):
    line1 = list1[i].replace("\n","")
    line2 = list2[i].replace("\n","")
    if line1 != line2:
        difflines.append(i)
        list3.append(line1)
        list4.append(line2)
print(difflines)
print(list3)
print(list4)

        
