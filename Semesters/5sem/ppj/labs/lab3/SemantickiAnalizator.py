import sys

#treba odvojit varijable od operatora!!!!

stack = []
log = []


def checkVar(var):
    print("checking")
    for map in stack:
        print(map)
        if var in (map.keys()):
            return map,True
    return False    

def forLoop(i:int,code:list):
    print("forLoop ",i+1)
    k=1
    forVars = {}
    parts = code[i].split(" ")

    stack.append(forVars)

    #obradi ZA liniju
    forVars[parts[1]] = i+1

    i = i + 1
    print(forVars)

    while code[i] != "az":
        parts = code[i].split(" ")
        if parts[0] == "za":
            i = i + forLoop(i,code)
            continue
        else:
            if not (checkVar(parts[0])):
                forVars[parts[0]] = i+1
            for j,part in enumerate(parts[2::]): #bolje od 3
                if part[0].isalpha():
                    theMap,cond = checkVar(part)
                    if cond:
                        log.append(f"{i+1} {theMap[part]} {part}")
                    else:
                        print(f"err {i+1} {part}")    
                        exit(0)
        i = i + 1
        k = k + 1  
        #print("increment k",k)              
    stack.pop() 
    #print(k)
    return k   

defVar = {} #kljuc var, value redak def
grammar = ["$","<program>","<lista_naredbi>","<naredba>","<naredba_pridruzivanja>","<za_petlja>","<E>","<E_lista>","<T>","<T_lista>","<P>"]
code = [""]
string = ""

stack.append(defVar)

for line in sys.stdin:
    if line in ("", "\n"):
        break
    elif line.strip() in (grammar):
        continue
    line = line.strip()
    #print(line)
    thing = line.split(" ")[2]
    row = int(line.split(" ")[1])
    if row > len(code):
        code.append(thing)
        string = string + "\n" + thing
        #print(code[row-1])
    else:
        code[row-1] = code[row-1] + " " + thing
        string = string + " " + thing
        #print(code[row-1])   

string = string[1::]
code[0] = code[0][1::]

#print(string)
i = 0
while i < len(code):
    print(i+1)
    parts = code[i].split(" ")

    if parts[0] == "za":
        i = i + forLoop(i,code)
        continue
    else:
        if not (parts[0] in (defVar.keys())):
            defVar[parts[0]] = i+1
        for j,part in enumerate(parts[2::]): 
            if part[0].isalpha():
                if part in (defVar.keys()):
                    log.append(f"{i+1} {defVar[part]} {part}")
                else:
                    print(f"err {i+1} {part}")    
                    exit(0)


print(log)
#print(defVar.keys())
#print(code)
#print(string[1::])
# br_red_kor br_red_def lek_jed
# err br_red lek_jed