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
    def __init__(self, feature,subtrees,most_common_class):
        self.feature = feature
        self.subtrees = subtrees #tuple list?
        self.most_common_class = most_common_class

    def copy(self):
        new_node = Node(self.feature,copy.deepcopy(self.subtrees),self.most_common_class)
        return new_node



class ID3:
    def __init__(self,depth):
        self.depth = depth
        self.root = None
        self.features = None
        self.classes = None

    def argmax(self,dataset, X=None):
        if X:
            #for IG
            IGs = {}
            for x in X:
                IGs[x] = information_gain(dataset,self.features.index(x))
            for key in IGs.keys():
                print(f"IG({key}):{round(IGs[key],4)} ",end='')
            print()
            IGs = dict(sorted(IGs.items()))
            #print(max(IGs, key=IGs.get))
            return max(IGs, key=IGs.get)
        else:
            #for |D(y=v)|
            classes = [row[-1] for row in dataset]
            class_counts = Counter(classes)
            class_counts = dict(sorted(class_counts.items()))

            return max(class_counts,key=class_counts.get)


    def _id3_algorithm(self,dataset,parent_dataset,X,depth):
        if not dataset:
            v = self.argmax(parent_dataset)
            print("first:",v)
            return Leaf(v)
        most_common_class = self.argmax(dataset)
        dataset_v = [row for row in dataset if row[-1] == most_common_class]

        if not X or sorted(dataset_v) == sorted(dataset) or depth == 0: 
            print("second:",most_common_class)
            return Leaf(most_common_class) #????

        x = self.argmax(dataset,X)

        subtrees = []
        values_of_x = set(row[self.features.index(x)] for row in dataset) #pazi na dataset koji se koristi, mozda globalni cijeli?
        
        for v in values_of_x:
            dataset_x = [row for row in dataset if row[self.features.index(x)] == v]
            #print("datasetx:")
            #print(dataset_x)
            t = self._id3_algorithm(dataset_x,dataset,[feature for feature in X if feature != x],depth-1)
            subtrees.append((v,t)) #valjda????

        print("third")
        return Node(x,subtrees,most_common_class)    


    def fit(self,train_dataset):
        #training the model
        self.features, data, self.classes = read_file(train_dataset)
        self.features = self.features[:-1]
        feats = self.features.copy()
        self.root = self._id3_algorithm(data,data,feats,self.depth)


    def predict(self,test_dataset):
        #predict result
        _, data, _ = read_file(test_dataset)

        correct = 0
        incorrect = 0
        predictions = ""
        classes = set(row[-1] for row in data)
        confusion_matrix = {actual: {predicted: 0 for predicted in classes} for actual in classes}

        for row in data:

            root = self.root #useless?
            
            while True:
                if isinstance(root,Leaf):
                    #print("prediciton:", root.value)
                    prediction = root.value
                    predictions += prediction + " "
                    actual = row[-1]
                    if root.value == actual:
                        correct += 1
                    else:
                        incorrect += 1

                    confusion_matrix[actual][prediction] = confusion_matrix[actual].get(prediction, 0) + 1
                    break

                idx = self.features.index(root.feature)

                found = False
                for tuple in root.subtrees:
                    if tuple[0] == row[idx]:
                        found = True
                        root = tuple[1]

                if not found:
                    #print("TEST!!!!!!")
                    prediction = root.most_common_class
                    confusion_matrix[actual][prediction] = confusion_matrix[actual].get(prediction, 0) + 1
                    actual = row[-1]
                    if root.value == actual:
                        correct += 1
                    else:
                        incorrect += 1

        accuracy = correct/(correct+incorrect)
        print("[PREDICTIONS]:",predictions[:-1])
        print("[ACCURACY]:", round(accuracy,5))
        print("[CONFUSION MATRIX]:")
        for actual_class in sorted(confusion_matrix.keys()):
            predictions = confusion_matrix[actual_class]
            matrix_row = ""
            for predicted_class in sorted(predictions.keys()):
                #print(f"{predictions[predicted_class]} ", end='')
                matrix_row += f'{predictions[predicted_class]} '
            print(matrix_row[:-1])

            
    def _print_step(self,elements,string,depth):
        if isinstance(elements[1],Leaf):
            print(string, elements[1].value)
            return
        
        for element in elements[1].subtrees:
            new_string = string + f' {depth}:{elements[1].feature}={element[0]}'
            self._print_step(element,new_string,depth+1)

    def print_tree(self):
        print(self.root.feature,self.root.subtrees)
        print("[BRANCHES]:")

        if isinstance(self.root,Leaf):
            print(self.root.value)
            return
        root = self.root.copy()
        depth = 1
        string = ""
        #print(root.subtrees)
        for element in root.subtrees:
            string = f'{depth}:{root.feature}={element[0]}'
            self._print_step(element,string,depth+1)
            #print()
   
def main():
    #path = '../../files/'
    #train_dataset = path + 'logic_small.csv'
    #test_dataset = path + 'logic_small_test.csv'
    train_dataset = sys.argv[1]
    test_dataset = sys.argv[2]
    depth = None
    try:
        depth = sys.argv[3]
    except:
        depth = 100000000000
    depth = 1
    model = ID3(depth)
    #print (model.depth)
    model.fit(train_dataset)
    #print()
    model.print_tree()
    #print("end fit")
    #exit()
    predictions = model.predict(test_dataset)


if __name__ == '__main__':
    main()