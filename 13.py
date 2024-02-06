def transform1(file1):
    f1 = open(file1,"r")
    list1 = f1.read().split("\n")
    len1 = len(list1)
    list2 = []
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for j in range(0,26,1):
        templist = []
        for i in range(0,len1,1):
            if list1[i][0] == alpha[j]:
                templist.append(list1[i])  
        list2.append(templist)      
    return list2
def transform2(word2):
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    list2 = transform1("words.txt")
    input1 = word2
    len2 = len(input1)
    lastChar = input1[len2-1:len2]
    position = alpha.index(lastChar)
    list3 = list2[position]
    return list3
input1 = "water"
list3 = transform2(input1)
input2 = list3[0]
print(input1,input2)

input1 = "train"
list3 = transform2(input1)
input2 = list3[0]
print(input1,input2)

input1 = "trainer"
list3 = transform2(input1)
input2 = list3[0]
print(input1,input2)
