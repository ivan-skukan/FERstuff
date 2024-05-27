import random
from math import e

def sigmoid(x):
    return 1 / (1 + e**(-x))

def dot_product(matrix,vector):
    result_vector = []

    for row in matrix:
        sum = 0
        for i,element in enumerate(row):
            try:
                sum += element*vector[i]
            except IndexError:
                print('Matrix and vector incompatible')
        result_vector.append(sum)

    return result_vector

class NN:
    def __init__(self,input_size,hidden_layers):
        self.input_size = input_size
        self.weights = {}
        self.layers = [input_size] + hidden_layers + [1] #check lol
        self._init_weights()

    def _init_weights(self):
        nn_depth = len(self.layers)

        for layer in range(1,nn_depth):
            self.weights['w' + str(layer)] = [[random.gauss(0,0.01) for _ in range(self.layers[layer-1])] for _ in range(self.layers[layer])]
            self.weights['b' + str(layer)] = [0.0 for _ in range(self.layers[layer])]

    def evaluate(self,dataset): #not sure yet about this
        results = []
        expected_results = []
        for sample in dataset:
            output = self.forward(sample[:-1])
            results.append(output)
            expected_results.append(sample[-1])
        
        err = self.mean_sq_err(expected_results,results,len(dataset))

        return err


    def forward(self,X: list):
        output = X.copy()
    
        for i in range(len(self.layers)):
            key_weights = 'w' + str(i+1)
            key_bias = 'b' + str(i+1)
            weights = self.weights[key_weights]
            biases = self.weights[key_bias]
            output = dot_product(weights,output) + biases
            output = [sigmoid(x) if i != len(self.layers) - 1 else x for x in output]

        return output
    
    def mean_sq_err(self,expected_results,results,N):
        L = len(expected_results)
        sum = 0

        for i in range(L):
            sum += (expected_results[i] - results[i]) ** 2

        return sum/N
    
    def copy(self,other):
        layers_copy = other.layers.copy()
        return NN(other.layers[0],layers_copy[1:-1])