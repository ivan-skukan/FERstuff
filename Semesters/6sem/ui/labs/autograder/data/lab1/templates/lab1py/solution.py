import sys
import os

class Node:
    def __init__(self,state,neighbours):
        self.state = state
        self.neighbours = neighbours
    


os.chdir(os.path.dirname(os.path.abspath(__file__))) #privremeno, mozda izbrisem

print(os.getcwd()) 

def main():
    args = sys.argv[:1]
    alg = args[1]
    file = args[2]
    heur = args[3]

    path = '../../files/'

    os.chdir(path)

    try:
        with open(file, 'r') as state_file:
            lines = state_file.readlines()
    except FileNotFoundError:
        print(f"File not found,exiting")
        return
    
    start = lines[0]
    goal = lines[1]

    for line in lines[2:]:
        parent_state = line.split(':')[0]
        neighbour_info = line.split(':')[1]
        


if __name__ == "__main__":
    main()
