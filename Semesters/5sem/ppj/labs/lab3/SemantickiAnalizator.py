import sys


defVar = {} #kljuc var, value redak def
grammar = [] #ovdje stavis nezavrsne znakove gramatike za skippat
code = []
tree = []

for line in sys.stdin:
    #print(line)
    #print(line.strip())
    tree.append(line.strip())

for line in tree:
    if line in grammar:
        continue
    thing = line.split(" ")[2]
    row = int(line.split(" ")[1])
    code[row] = code[row] + thing



# br_red_kor br_red_def lek_jed
# err br_red lek_jed
