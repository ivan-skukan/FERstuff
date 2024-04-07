import argparse
import os
import sys
import heapq
from collections import deque
from resolution import plResolution

#possible ways to remember parent clauses?
#dictionary with clause as key and parent clauses as value?
#class?

def parse_clause_file(clause_file):
    clauses = set()
    final = set()

    with open(clause_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        final = frozenset(lines[-1].strip().lower().split(' v '))

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
    #input_file = sys.argv[3] #later
    
    #to be implemented?
    #parser = argparse.ArgumentParser() 
    clause_file = '../../../data/lab2/files/resolution_small_example_3.txt'
    #za new_example_6 a is true
    #coffe or tea pada
    #coffe or tea nopowder pada
    try:
        clauses, toProveClause = parse_clause_file(clause_file)
    except FileNotFoundError:
        print("Error: Could not parse clause file, exiting")
        exit(1)
    result = plResolution(clauses,toProveClause)
    toProveClause = list(toProveClause)
    toProveClauseString = ""
    for clause in toProveClause:
        #print(clause)
        toProveClauseString += " v " + clause
    toProveClauseString = toProveClauseString[3:]    
    result = "true" if result else "unknown"
    print(f"[CONCLUSION] : {toProveClauseString} is {result} ")
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