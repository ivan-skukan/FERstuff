def splitNumsAndWords(i, word):
    j = 0
    str = ""
    nums = ""

    if(word != '' and word[0].upper() >= 'A'):
        while(j < len(word) and word[j].upper() >= 'A' and word[j].upper() <= 'Z'):
            str += word[j]
            j += 1
        while(j < len(word) and word[j] >= '0' and word[j] <= '9'):
            nums += word[j]
            j += 1
    else:
        while(j < len(word) and word[j] >= '0' and word[j] <= '9'):
            nums += word[j]
            j += 1
        while(j < len(word) and word[j].upper() >= 'A' and word[j].upper() <= 'Z'):
            str += word[j]
            j += 1

    if(word[0] >= 'A'):    
        print(f"IDN {i+1} {word}")
        #if(nums != ""):
         #   print(f"BROJ {i+1} {nums}")     
    else:
        print(f"BROJ {i+1} {nums}") 
        if(str != ""):
            print(f"IDN {i+1} {str}")
##################        
inp = []

while True:
    try:
        enter = input()
        inp.append(enter) 
    except EOFError:
        break
       
strings = inp
row = 0

myMap = {}
myMap["za"] = "KR_ZA"
myMap["az"] = "KR_AZ"
myMap["od"] = "KR_OD"
myMap["do"] = "KR_DO"
myMap["+"] = "OP_PLUS"
myMap["-"] = "OP_MINUS"
myMap["/"] = "OP_DIJELI"
myMap["*"] = "OP_PUTA"
myMap["("] = "L_ZAGRADA"
myMap[")"] = "D_ZAGRADA"
myMap["="] = "OP_PRIDRUZI"

checkBreak = False
#print(strings)

for i in range(0,len(strings)):
    if(strings[i] == ''):
        continue
    if(checkBreak):
        checkBreak = False
        continue

    str = strings[i].split(" ")

    a = 0
    while '' in str:
        str.remove('')
    #print(str)

    for j in range(0,len(str)):

        if(checkBreak):
            checkBreak = False
            break

        word = str[j]
        word = ' '.join(word.split())
        if word in myMap:
            print(myMap[word] + f" {i+1} " + word)
        elif (word == "//"):
            break
        else:
            check = word.count('+') + word.count('-') + word.count('*') + word.count('/') + word.count('=') + word.count('(') + word.count(')')
            if(check):
                idn = ""
                k = 0
                while(k < len(word)):
                    if(k + 1 < len(word) and  word[k] == '/' and word[k+1] == '/'):
                        checkBreak = True
                        break
                    while(k < len(word) and word[k] not in myMap):
                        idn += word[k]
                        k += 1
                    if(idn != ""):
                        if(idn[0].upper() >= 'A' and idn[0].upper() <= 'Z'):
                            print(f"IDN {i+1} {idn}")    
                        else:
                            print(f"BROJ {i+1} {idn}")    
                        idn = ""
                    else:
                        print(myMap[word[k]] + f" {i+1} {word[k]}")  
                        k += 1  
                    #print(k)     
            else:  
                if(word!=''): 
                    splitNumsAndWords(i,word)  
