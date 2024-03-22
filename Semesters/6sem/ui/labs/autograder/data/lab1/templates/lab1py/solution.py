import sys
import os
import heapq
from collections import deque

class Node:
    def __init__(self,state):
        self._state = state
        self._neighbours = {}
        self._parent = None
        self._heur = None
        self._cost = 0
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self,state):
        self._state = state #probably wont need it

    @property
    def neighbours(self): #mozda bolje mapa za laksi dohvat vrijednosti?
        return self._neighbours
    
    @neighbours.setter
    def neighbours(self,neighbours):
        self._neighbours = neighbours

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self,node):
        self._parent = node
    
    @property
    def heur(self):
        return self._heur
    
    @heur.setter
    def heur(self, heur):
        self._heur = heur

    @property
    def cost(self):
        return self._cost
    
    @cost.setter
    def cost(self, cost):
        self._cost = cost

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._state == other._state
        return False

    def __hash__(self):
        return hash(self._state)

    def __lt__(self, other):
        return self._state < other._state	    

#os.chdir(os.path.dirname(os.path.abspath(__file__))) #privremeno, mozda izbrisem

def A_star(start: Node, nodes: dict, goal: list):
    open = [(start._heur, start)]
    open_set = set([start._state]) #dodat skip list? micanje iz heapa nije efikasno
    visited = set()

    while open:
        currentCost, node = heapq.heappop(open) #currentCost je kriv
        open_set.remove(node._state)
        visited.add(node._state)

        if node._state in goal:
            return node, len(visited)

        for neighbour in node.neighbours.keys():
            neighbourNode = nodes[neighbour]
            price = node.neighbours[neighbour]
            if (neighbour in visited or neighbour in open_set):
                if neighbourNode._cost > (currentCost + price) or (neighbourNode._cost == 0 and neighbourNode._state != start._state):
                    oldCost = neighbourNode._cost
                    neighbourNode._cost = currentCost + price
                    neighbourNode._parent = node
                    #if neighbour in open_set:
                     #   open.remove((oldCost + neighbourNode._heur, neighbourNode))
                      #  open_set.remove(neighbour)
                    #if neighbour in visited:
                     #   visited.remove(neighbour)  
                else:
                    continue
            else:   
                neighbourNode._parent = node
                neighbourNode._cost = currentCost + price
            heapq.heappush(open, (currentCost + price + neighbourNode._heur, neighbourNode))
            open_set.add(neighbourNode._state)
    return False, 0

#UCS algorithm
#source: lectures and slides
#some used structures:
#heapq for fast access to data
#set for quick addition
def UCS(start: Node, nodes: list, goal: list):
    open = [(0, start)]#tuples?
    #open_set = set([start._state])
    visited = set()

    while open:
        #node, currentCost = open.popleft()
        currentCost, node = heapq.heappop(open)
        #open_set.remove(node._state)
        visited.add(node._state)

        if node._state in goal:
            return node, len(visited)

        neighbours = []

        for neighbour in node.neighbours.keys():
            neighbourNode = nodes[neighbour]
            price = node.neighbours[neighbour]
            #if neighbourNode._state not in open_set and neighbourNode._state not in visited:
            if neighbourNode._state not in visited:
                
                if neighbourNode._cost > currentCost + price or neighbourNode._cost == 0: #if cost is 0, it means it was not visited yet, else if its in queue check if new cost is lower
                    neighbourNode._parent = node
                    neighbourNode._cost = currentCost + price
                #neighbours.append((neighbourNode, currentCost + price))
                heapq.heappush(open, (currentCost + price, neighbourNode))
                #open_set.add(neighbourNode._state)
        neighbours.sort(key=lambda x: x[1])
        #open.extend(neighbours)
        #print(node._state, currentCost)

    return False, 0

#Breadth first search algorithm
#source: lectures and slides
def BFS(start: Node,nodes: dict,goal: list):
    #open = [start]
    open = deque([start])
    #additional set for quicker access to elements
    open_set = set([start._state])
    visited = set()

    while open:
        node = open.popleft()
        open_set.remove(node._state)
        visited.add(node._state)
        if node._state in goal:
            return node, len(visited)
        neighbours = []
        for neighbour in node.neighbours.keys():
            #print(neighbour)
            #print(neighbour[0]._state)
            neighbourNode = nodes[neighbour]
            #if neighbourNode._state not in open_set and neighbourNode._state not in visited:
            if neighbourNode._state not in visited and neighbourNode._state not in open_set:
                neighbourNode._parent = node
                neighbours.append(neighbourNode)
                open_set.add(neighbourNode._state)
        neighbours.sort(key=lambda x: x) #treba li?
        open.extend(neighbours)


    return False, 0

#function to parse the file
def parse_file(file_path):
    nodes = []
    start = None
    goal = None
    with open(file_path, 'r', encoding='utf-8') as state_file:
        for line in state_file:
            if line.startswith('#'):
                continue
            parts = line.strip().split(':')
            state = parts[0]
            if start is None:
                start = Node(state)
                nodes.append(start)
                continue
            if goal is None:
                goal = parts[0].split(' ')
                continue
            node = Node(state)
            if not (node == start):
                nodes.append(node)
            else:
                node = start
            neighbours = parts[1][1:].split(' ')
            if neighbours[0] == '':
                continue
            for neighbour in neighbours:
                neighbour_parts = neighbour.split(',')
                node._neighbours[neighbour_parts[0]] = float(neighbour_parts[1])

    nodes_dict = {node._state: node for node in nodes}

    return start, nodes_dict, goal

#function to parse the heuristic file
def parse_heur(file_path, nodes):
    with open(file_path, 'r', encoding='utf-8') as state_file:
        for line in state_file:
            parts = line.strip().split(':')
            state = parts[0]
            node = nodes[state]
            node._heur = float(parts[1][1:])

#function to print the results
def print_stuff(alg, success, statesVisited, pathLength, cost, path):
    print(success)
    print("[STATES_VISITED]: " + str(statesVisited))
    print("[PATH_LENGTH]: " +  str(pathLength))
    if alg == "BFS":
        print("[TOTAL_COST]: -")
    else:
        print("[TOTAL_COST]: ", cost)
    print("[PATH]: ",path)

def main():
    #args = sys.argv[1:]
    #alg = args[1]
    #file = args[2]
    #heur = args[3]
    alg = "A-STAR"
    file = "istra.txt"
    heur = "istra_pessimistic_heuristic.txt"
    #istra_pessimistic_heuristic.txt
    #za ostale su putevi tocni ali cijene krive

    path = '../../files/'

    #print(os.getcwd())
    os.chdir(path)
    #print(os.getcwd())
    try:
        start, nodes, goal = parse_file(file)
    except FileNotFoundError:
        print("File not found, exiting")
        return

    try:
        parse_heur(heur, nodes)
    except FileNotFoundError:
        print("Heuristic file not found, exiting")
        return
    
    success = "[FOUND_SOLUTION]: "
    path = ""
    pathLength = 1

    if alg == "BFS":
        final, statesVisited = BFS(start, nodes, goal)
        print("# BFS")
        if final:
            path = final._state + path
            success += "yes"
            
            while final:
                #print(final._state)
                final = final._parent
                if final:
                    path = final._state + " => " +  path
                    pathLength += 1
                
        else:
            success += "no"    
            print(success)
            return

        print_stuff(alg, success, statesVisited, pathLength, 0, path)
#################################################################
    if alg == "UCS":
        final, statesVisited = UCS(start, nodes, goal)
        print("# UCS")
        if final:
            cost = final.cost
            path = final._state + path
            success += "yes"
            
            while final:
                #print(final._state)
                final = final._parent
                if final:
                    path = final._state + " => " +  path
                    pathLength += 1
        else:
            success += "no"
            print(success)
            return
        
        print_stuff(alg, success, statesVisited, pathLength, cost, path)

    if alg == "A-STAR":
        final, statesVisited = A_star(start, nodes, goal)
        print("# A*")
        if final:
            cost = final.cost
            path = final._state + path
            success += "yes"
            
            while final:
                #print(final._state)
                final = final._parent
                if final:
                    path = final._state + " => " +  path
                    pathLength += 1
        else:
            success += "no"
            print(success)
            return
        
        print_stuff(alg, success, statesVisited, pathLength, cost, path)



if __name__ == "__main__":
    main()
