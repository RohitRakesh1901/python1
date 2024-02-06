import mod_difference as md
fname1 = "file1.txt"
fname2 = "file2.txt"
f1 = open(fname1,"r")
f2 = open(fname2,"r")
list1 = f1.readlines()
list2 = f2.readlines()
result = md.diff1(fname1,fname2)
print(result)
lenr = len(result)

for j in range(0,lenr,1):
    lineno = result[j]
    list3 = list1[lineno].replace("\n","").split(" ")
    list4 = list2[lineno].replace("\n","").split(" ")
    len3 = len(list3)
    for i in range(0,len3,1):
        word1 = list3[i]
        word2 = list4[i]
        if word1 != word2:
            print(word1,word2)
            
            
            


