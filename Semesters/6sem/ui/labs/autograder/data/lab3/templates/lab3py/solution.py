import sys
import math
import csv
from collections import Counter
import copy


def entropy(x):
    return 0 if x==0 else x*math.log(x,2)

def information_gain(dataset,x_index):
    #print("x-index:",x_index)
    classes = [row[-1] for row in dataset]
    class_counts = Counter(classes)
    #print(class_counts)
    total_entropy = 0

    for label in class_counts.keys():
        #print(class_counts[label],len(dataset))
        total_entropy += entropy(class_counts[label]/len(dataset))
        
    
    total_entropy = -1 * total_entropy

    values_of_x = set(row[x_index] for row in dataset)
    #print(values_of_x)
    sum = 0

    for x in values_of_x:
        dataset_x = [row for row in dataset if row[x_index] == x]
        classes = [row[-1] for row in dataset_x]
        class_counts = Counter(classes)
        entropy_x = 0
        for label in class_counts.keys():
            #print("ratio:",class_counts[label],len(dataset_x))
            entropy_x += entropy(class_counts[label]/len(dataset_x))
        #print("partial entropy:",entropy_x)
        sum += len(dataset_x) * (-1) * entropy_x

    #print(total_entropy)
    #print(sum / (len(dataset)))
    #print("IG:",total_entropy - sum / len(dataset))
    #exit()
    return total_entropy - sum / len(dataset)
    

def read_file(file):

    features = set() #set?
    data = []
    classes = set()
    
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        features = reader.fieldnames
        for row in reader:
            data.append(list(row.values()))
            classes.add(row[features[-1]])

    return features, data, classes

class Leaf:
    def __init__(self,value):
        self.value = value

class Node:
    def __init__(self, feature,subtrees):
        self.feature = feature
        self.subtrees = subtrees #tuple list?

    def copy(self):
        new_node = Node(self.feature,copy.deepcopy(self.subtrees))
        return new_node



class ID3:
    def __init__(self):
        self.root = None
        self.features = None
        self.classes = None

    def argmax(self,dataset, X=None):
        if X:
            #for IG
            IGs = {}
            for x in X:
                IGs[x] = information_gain(dataset,self.features.index(x))

            #print(IGs)
            #exit()
            IGs = dict(sorted(IGs.items()))
            return max(IGs, key=IGs.get)
        else:
            #for |D(y=v)|
            classes = [row[-1] for row in dataset]
            class_counts = Counter(classes)
            max_class = max(class_counts,key=class_counts.get)

            return max_class


    def _id3_algorithm(self,dataset,parent_dataset,X):
        if not dataset:
            v = self.argmax(parent_dataset)
            #print("bitchasssss1")
            return Leaf(v)
        v = self.argmax(dataset)
        #print(v)
        dataset_v = [row for row in dataset if row[-1] == v]
        #print("nigga2????")

        if not X or sorted(dataset_v) == sorted(dataset): #check for order
            #print("bitchasssss2")
            return Leaf(v) #????
        #print("NIGGAAAA")
        x = self.argmax(dataset,X)
        #print("nigga3????")
        subtrees = []
        values_of_x = set(row[self.features.index(x)] for row in dataset) #pazi na dataset koji se koristi, mozda globalni cijeli?
        
        for v in values_of_x:
            dataset_x = [row for row in dataset if row[self.features.index(x)] == v]
            #print("datasetx:")
            #print(dataset_x)
            t = self._id3_algorithm(dataset_x,dataset,[feature for feature in X if feature != x])
            subtrees.append((v,t)) #valjda????

        return Node(x,subtrees)    


    def fit(self,train_dataset):
        #training the model
        self.features, data, self.classes = read_file(train_dataset)
        self.features = self.features[:-1]
        feats = self.features.copy()
        self.root = self._id3_algorithm(data,data,feats)


    def predict(self,test_dataset):
        #predict result
        _, data, _ = read_file(test_dataset)

        correct = 0
        incorrect = 0
        
        for row in data:
            root = self.root.copy() #useless?
            #for x in row[:-1]:
                

    def _print_step(self,elements,string,depth):
        if isinstance(elements[1],Leaf):
            print(string, elements[1].value,end="\n")
            return
        
        for element in elements[1].subtrees:
            new_string = string + f' {depth}:{elements[1].feature}={element[0]}'
            self._print_step(element,new_string,depth+1)

    def print_tree(self):
        #print(self.root.feature,self.root.subtrees)
        print("[BRANCHES]:")
        root = self.root.copy()
        depth = 1
        string = ""
        #print(root.subtrees)
        for element in root.subtrees:
            string = f'{depth}:{root.feature}={element[0]}'
            self._print_step(element,string,depth+1)
            #print()
   
def main():
    path = '../../files/'
    train_dataset = path + 'volleyball.csv'
    test_dataset = path + 'volleyball_test.csv'

    model = ID3()
    model.fit(train_dataset)
    #print()
    model.print_tree()
    print("end fit")
    #exit()
    predictions = model.predict(test_dataset)



if __name__ == '__main__':
    main()