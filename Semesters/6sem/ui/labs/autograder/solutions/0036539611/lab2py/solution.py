from resolution import plResolution
from resolution import negateFinal
import sys

def getPath(parentDict,parentKey,tuple,clauses):
    c1,c2 = tuple
    if c1 not in clauses:
        getPath(parentDict,c1,parentDict[c1],clauses)
    if c2 not in clauses:
        getPath(parentDict,c2,parentDict[c2],clauses)
    c1string = ""
    for literal in c1:
        c1string += ' v ' + literal
    c1string = c1string[3:]
    c2string = ""
    for literal in c2:
        c2string += ' v ' + literal
    c2string = c2string[3:]
    parentList = list(parentKey)
    resultString = ""  
    for literal in parentList:
        resultString += ' v ' + literal
    resultString = resultString[3:]
    #print(resultString)
    #print(parentKey)
    #exit()
    resultString = ""
    for literal in parentKey:
        resultString += ' v ' + literal
    resultString = resultString[3:]
    if parentKey == "NIL":
        print(f"{c1string} + {c2string} => {parentKey}")
        return
    print(f"{c1string} + {c2string} => {resultString}")


def printResult(clauses,toProveClause,parentDict):
    final = negateFinal(toProveClause)
    i = 1
    for clause in clauses:
        #print(clause)
        #print(clauses)
        lineString = ""
        for literal in clause:
            lineString += ' v ' + literal
        lineString = lineString[3:]
        print(f"{i}. {lineString}")
        i += 1
    finalString = ""
    for literal in final:
        finalString += ' v ' + list(literal)[0]
    finalString = finalString[3:]        
    print(f"{i}. {finalString}")
    print("===============")
    #i += 1
    #print(final)
    #print(clauses)
    clauses.update(final)
    #print(clauses)
    #exit()
    getPath(parentDict,"NIL",parentDict["NIL"],clauses) #check

def parse_clause_file(clause_file):
    clauses = set()
    final = set()

    with open(clause_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        final = frozenset(lines[-1].strip().lower().split(' v '))
        global lastline
        lastline = lines[-1].strip().lower()

        for i,line in enumerate(lines):
            if line.startswith('#'):
                continue
            if i == (len(lines) - 1):
                continue
            clauses.add(frozenset(line.strip().lower().split(' v ')))

        #if final in clauses:
            #clauses.remove(final)
    return clauses, final

def parse_input_file(input_file):
    commands = set()
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            commands.add(line.strip())
    return commands

def main():
    #res_cook = sys.argv[1]
    #clause_file = sys.argv[2]
    #if res_cook == "cooking":
        #input_file = sys.argv[3] #later

    clause_file = '../../../data/lab2/files/new_example_5.txt'
    try:
        clauses, toProveClause = parse_clause_file(clause_file)
    except FileNotFoundError:
        print("Error: Could not parse clause file, exiting")
        exit(1)
    result, parentDict = plResolution(clauses,toProveClause)
    toProveClause = list(toProveClause)
    #output = getSolutionPath(parentDict)
    result = "true" if result else "unknown"
    if result == "true":
        printResult(clauses,toProveClause,parentDict)
    print(f"[CONCLUSION]: {lastline} is {result} ")
    """ #later
    if(res_cook == "cooking"):
        try:
            returns_cook = parse_input_file(input_file)
            #commands?
        except FileNotFoundError:
            print("Error: Could not parse input file, exiting")          
    """
if __name__ == "__main__":
    main()