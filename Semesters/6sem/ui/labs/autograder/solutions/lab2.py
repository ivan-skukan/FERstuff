import argparse
import os
import sys
import heapq
from collections import deque

def parse_clause_file(clause_file):
    atoms = set()
    clauses = set() #[]?

    with open(clause_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            if " v " not in line:
                atoms.add(line.strip().lower())
                continue
            clauses.add(line.strip().lower())
    return atoms, clauses    

def parse_input_file(input_file):
    commands = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            commands.append(line.strip())
    return commands

def main():
    res_cook = sys.argv[1]
    clause_file = sys.argv[2]
    input_file = sys.argv[3] #throws error if not provided

    #to be implemented
    #parser = argparse.ArgumentParser() 

    try:
        atoms, clauses = parse_clause_file(clause_file)
    except:
        print("Error: Could not parse clause file, exiting")

    if(res_cook == "cooking"):
        try:
            returns_cook = parse_input_file(input_file)
            #commands?
        except FileNotFoundError:
            print("Error: Could not parse input file, exiting")          

if __name__ == "__main__":
    main()