import itertools

NIL = "NIL"
parentDict = {}

def negateFinal(finalClause):
    newClauses = set()

    for literal in finalClause:
        notLiteral = literal[1:] if literal[0] == '~' else '~' + literal
        #newClauses.add(notLiteral)
        #print(notLiteral)
        newClauses.add(frozenset([notLiteral]))
    #newClauses = frozenset(newClauses) #CHECK!!!!
    #print(newClauses)
    #exit()
    return newClauses

#check if clause2 is a subset of clause1
def isSubset(clause1,clause2):
    return clause2.issubset(clause1)

#use simplification strategy of erasing unnecessary information
def simplify(clauses):
    #A v A = A ? should be resolved due to sets
    #print("clauses:",clauses)
    newClauses = set()
    for c1 in clauses:
        addClause = True

        for l1 in c1:
            notl1 = l1[1:] if l1[0] == '~' else '~' + l1 
            if notl1 in c1: #tautology check
                addClause = False
                break
        for c2 in clauses:
            if c1 is not c2:
                if c2.issubset(c1): #if c1 is a superset, remove it
                    addClause = False
                    break
        if addClause:
            newClauses.add(c1)

    return frozenset(newClauses)     


def plResolve(c1,c2):
    #literals1 = set(c1.split(' v '))
    #literals2 = set(c2.split(' v '))
    resolvents = set()
    #print(c1,c2)
    for l1 in c1:
        notl1 = l1[1:] if l1[0] == '~' else '~' + l1

        if notl1 in c2:
            #print("found something")
            if len(c1) == 1 and len(c2) == 1:
                resolvents.add(frozenset(["NIL"])) #NOVO, trebalo bi bit ok
                break #!!!!!!!!!!!!
            newClause = set(c1.copy()) | set(c2.copy()) #union
            newClause.remove(notl1)
            newClause.remove(l1)

            newClause = frozenset(newClause)
            resolvents.add(newClause) 
            #break
#YOOOOOOOOOOO
    return resolvents

def plResolution(clauses, finalClause):
    SOSclauses = set()
    SOSclauses.update(negateFinal(finalClause)) #valjda, triple check!!!!
    #print(SOSclauses)
    #print("clauses before:",clauses)
    clauses = simplify(clauses)
    #print("clauses after:",clauses)
    #SOScopy = SOSclauses.copy()
    #clausesCopy = clauses.copy()

    allClauses = set()
    allClauses.update(SOSclauses)
    allClauses.update(clauses)
    #print(allClauses)
    #exit()
    new = set()
    checked = {}
    global parentDict

    while True:
        #print("loop0")
        SOScopy = SOSclauses.copy()
        for c1 in allClauses: #original clauses?
            #print("loop1")
            #print(i)
            #i += 1
            for c2 in SOSclauses: #original clauses?
                #print("loop2")
                #print(c1,c2)
                #print(j)
                #j += 1
                if c1 == c2 or (c1,c2) in checked or (c2,c1) in checked: #NOVO
                    continue
                checked[(c1,c2)] = None
                resolvents = plResolve(c1,c2)
                #print(resolvents)
                resolvents = simplify(resolvents)
                if frozenset([NIL]) in resolvents: #NOVO
                    parentDict["NIL"] = (c1,c2)
                    return True, parentDict
                
                #resolvents = simplify(resolvents) #check!!!! ovo prvo?
                #resolvents je frozen(frozen())??
                #print(resolvents)
                new.update(resolvents) #ovo drugo?
                if not (resolvents.issubset(SOScopy)):
                    SOScopy.update(new)
                checked[(c1,c2)] = resolvents
                if len(resolvents) > 0:
                    parentDict[list(resolvents)[0]] = (c1,c2) #novo
                #print(new)

        if new.issubset(allClauses):
            return False, parentDict
        allClauses.update(new) 
        #if not (new.issubset(SOSclauses)):
            #SOSclauses.update(new)
        SOSclauses = SOScopy.copy()    
        #print(SOSclauses)
        #exit()
    
 