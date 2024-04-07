import itertools

NIL = frozenset("NIL")

def negateFinal(finalClause):
    newClauses = set()

    for literal in finalClause:
        notLiteral = literal[1:] if literal[0] == '~' else '~' + literal
        newClauses.add(notLiteral)
    newClauses = frozenset(newClauses) #CHECK!!!!
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
                if c2.issubset(c1): #check if c1 is a superset of c2. If so, remove it
                    addClause = False
                    break
        if addClause:
            newClauses.add(c1)

    return newClauses     


def plResolve(c1,c2):
    #print("resolving")
    #literals1 = set(c1.split(' v '))
    #literals2 = set(c2.split(' v '))
    resolvents = set()
    #print(c1,c2)
    for l1 in c1:
        notl1 = l1[1:] if l1[0] == '~' else '~' + l1

        if notl1 in c2:
            #print("found something")
            if len(c1) == 1 and len(c2) == 1:
                resolvents.add(NIL)
            newClause = set(c1.copy()) | set(c2.copy()) #union
            newClause.remove(notl1)
            newClause.remove(l1)
            #frozenset
            newClause = frozenset(newClause)
            resolvents.add(newClause) 

            #break

    return resolvents

def plResolution(clauses, finalClause):
    SOSclauses = set()
    SOSclauses.add(negateFinal(finalClause)) #valjda, triple check!!!!
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
    new = set()
    #i = 0 #debugging
    #j = 0
    checked = set() #novo!!!!!!!!

    while True:
        for c1 in allClauses: #original clauses?
            #print(i)
            #i += 1
            for c2 in SOSclauses: #original clauses?
                #print(c1,c2)
                #print(j)
                #j += 1
                if c1 == c2 or (c1,c2) in checked:
                    continue
                checked.add((c1,c2))
                resolvents = plResolve(c1,c2)
                #print(resolvents)
                if NIL in resolvents:
                    return True
                new.update(resolvents)
                resolvents = simplify(resolvents) #check!!!!

        if new.issubset(allClauses): #check #vjv mogu direkt 
            return False
        allClauses.update(new) 
        SOSclauses.update(new)
    
 