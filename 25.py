import mod_diffchecker as md
answers = md.diff2("file1.txt","file2.txt")
lena = len(answers)
for i in range(0,lena,1):
    print(answers[i])
