import sys
import csv
import argparse
from math import e
import random
from neuralnet import NN



def crossover(p1, p2):
    d = p1.copy()
    L = len(p1.layers)

    for i in range(1,L):
        key_w = 'w' + str(i)
        key_b = 'b' + str(i)

        weights_p1 = p1.weights[key_w]
        weights_p2 = p2.weights[key_w]
        biases_p1 = p1.weights[key_b]
        biases_p2 = p2.weights[key_b]

        #weights_d = d.weights[key_w]
        #biases_d = d.weights[key_b]

        average_w = [[(a+b)/2 for a,b in zip(row_p1,row_p2)] for row_p1,row_p2 in zip(weights_p1,weights_p2)]
        average_b = [(a+b)/2 for a,b in zip(biases_p1,biases_p2)]

        d.weights[key_w] = average_w
        d.weights[key_b] = average_b

    return d

def mutate(d,p,K):
     L = len(d.layers)

     for i in range(1,L):
        key_w = 'w' + str(i)
        key_b = 'b' + str(i)

        d.weights[key_w] = [[element + random.gauss(0, K) if random.random() <= p else element for element in row] for row in d.weights[key_w]]
        d.weights[key_b] = [element + random.gauss(0, K) if random.random() <= p else element for element in d.weights[key_b]]

def select_parent(P,evals):
    total = sum(evals)
    probabilities = [fitness/total for fitness in evals]

    cumulative_probability = 0
    threshold = random.random()

    for i,p in enumerate(P):
        cumulative_probability += probabilities[i]
        if cumulative_probability > threshold:
            return P
    return P[-1]
def generate_population(popsize, input_length, hidden_layers):
    P = []
    for _ in range(popsize):
        nn = NN(input_size=input_length, hidden_layers=hidden_layers)
        P.append(nn)
    return P

def parse_file(train_file):
    features = set()
    data = []
    with open(train_file, 'r') as f:
        reader = csv.DictReader(f)
        features = reader.fieldnames
        for row in reader:
            data.append(list(row.values()))
    return features,data
        
def parse_args(parser):
    parser.add_argument('--train', type=str, help='Path to the training dataset file')
    parser.add_argument('--test', type=str, help='Path to the testing dataset file')
    parser.add_argument('--nn', type=str, help='Neural network architecture')
    parser.add_argument('--popsize', type=int, help='Population size for the genetic algorithm')
    parser.add_argument('--elitism', type=bool, help='Elitism for the genetic algorithm')
    parser.add_argument('--p', type=float, help='Mutation probability for each chromosome element of the genetic algorithm')
    parser.add_argument('--K', type=float, help='Standard deviation of Gaussian noise mutation')
    parser.add_argument('--iter', type=int, help='Number of iterations for the genetic algorithm')

def main():
    #path = '../../files'
    #python solution.py --train sine_train.txt --test sine_test.txt --nn 5s --popsize 10 --elitism 1 --p 0.1 --K 0.1 --iter 10000
    parser = argparse.ArgumentParser(description='Read args for NN and CSV files')
    parse_args(parser)
    args = parser.parse_args()

    features_train,data_train = parse_file(args.train)
    _,data_test = parse_file(args.test)

    input_length = len(data_train[0])
    #input_length = 2
    hidden_layers = args.nn.split('s')
    #hidden_layers = [3,2]
    hidden_layers = [int(layer) for layer in hidden_layers if layer]

    #nn = NN(input_size=input_length, hidden_layers=hidden_layers)
    #print(nn.weights)
    #print(nn.layers)

    P = generate_population(args.popsize, input_length, hidden_layers)
    evals = [p.evaluate() for p in P]
    evals.sort()
    #evals.sort()
    P.sort(key=lambda p: p.last_eval)

    for iter in range(args.iter):
        new_P = set() #set?!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        for i in range(args.elitism):
            #new_P.add(P.pop())
            new_P.add(P[-(i+1)])
        for i in range(args.popsize):
            p1 = select_parent(P,evals)
            P.remove(p1)
            p2 = select_parent(P,evals)
            # Crossover using mean
            d = crossover(p1,p2)

            mutate(d,args.p,args.K)

            new_P.add(d)

        P = new_P
        evals = [p.evaluate() for p in P]
        #find the best while size < elitism ??
        if iter % 2000 == 0:
            print(f'[Train error @{iter}]: {max(evals)}')

    



if __name__ == '__main__':
    main()