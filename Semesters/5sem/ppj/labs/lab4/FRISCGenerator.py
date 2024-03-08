import sys

stack = []
log = []

def logPrint():
    for line in log:
        print(line)

def checkVar(var):
    for map in reversed(stack):
        if var in (map.keys()):
            return map,True
    return None,False    

def forLoop(i:int,code:list):
    k=1
    forVars = {}
    parts = code[i].split(" ")
    forVars[parts[1]] = i+1

    for part in parts[3::]:
        cond = checkVar(part)[1] and part[0].isalpha() 
        if part == parts[1]:
            logPrint()
            print(f"err {i+1} {part}")    
            exit(0)   
        if cond:
            log.append(f"{i+1} {checkVar(part)[0][part]} {part}")
        elif not checkVar(part)[1] and part[0].isalpha() and part not in ("od","do"):
            logPrint()
            print(f"err {i+1} {part}")    
            exit(0)    
    i = i + 1
    stack.append(forVars)
    #print(stack)

    while code[i] != "az":
        toAdd = False  
        add = ()
        parts = code[i].split(" ")
        if parts[0] == "za":
            increment = forLoop(i,code)
            i = i + increment
            k = k + increment
            continue
        else:
            if not (checkVar(parts[0])[1]):
                #forVars[parts[0]] = i+1
                toAdd = True
                add = (parts[0],i+1)
            for j,part in enumerate(parts[2::]):
                if part[0].isalpha():
                    theMap,cond = checkVar(part)
                    if cond:
                        log.append(f"{i+1} {theMap[part]} {part}")
                    else:
                        logPrint()
                        print(f"err {i+1} {part}")    
                        exit(0)
        if toAdd:
            forVars[add[0]] = add[1]
            toAdd = False                  
        i = i + 1
        k = k + 1
    #print("removing", stack[-1]," line ",i+1)             
    stack.pop() 
    return k+1 

defVar = {} 
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
    
    thing = line.split(" ")[2]
    row = int(line.split(" ")[1])
    if row > len(code):
        code.append(thing)
        string = string + "\n" + thing
    else:
        code[row-1] = code[row-1] + " " + thing
        string = string + " " + thing

string = string[1::]
code[0] = code[0][1::]
i = 0

#print(string,"\n")

while i < len(code):
    parts = code[i].split(" ")
    toAdd = False
    add = ()

    if parts[0] == "za":
        i = i + forLoop(i,code)
        continue
    else:
        if not (parts[0] in (defVar.keys())):
            #defVar[parts[0]] = i+1
            toAdd = True
            add = (parts[0],i+1)
        for j,part in enumerate(parts[2::]): 
            if part[0].isalpha():
                if part in (defVar.keys()):
                    log.append(f"{i+1} {defVar[part]} {part}")
                else:
                    logPrint()
                    print(f"err {i+1} {part}")    
                    exit(0)
        if toAdd:
            defVar[add[0]] = add[1]
            toAdd = False            
    i = i + 1                

logPrint()  