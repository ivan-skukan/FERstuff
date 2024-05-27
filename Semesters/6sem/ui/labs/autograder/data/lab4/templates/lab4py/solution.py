import sys
import csv
import argparse
from math import e
import random
from neuralnet import NN

def fitness(err):
    return 1/err

def crossover(p1, p2):
    d1 = p1.copy()
    d2 = p2.copy()

    

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

    #features_train,data_train = parse_file(args.train)
    #_,data_test = parse_file(args.test)

    #input_length = len(data_train[0])
    input_length = 2
    #hidden_layers = args.nn.split('s')
    hidden_layers = [3,2]
    hidden_layers = [int(layer) for layer in hidden_layers if layer]

    #nn = NN(input_size=input_length, hidden_layers=hidden_layers)
    #print(nn.weights)
    #print(nn.layers)

    P = generate_population(args.popsize, input_length, hidden_layers)
    evals = []
    for p in P:
        evals.append(fitness(p.evaluate(data_train)))

    for iter in range(args.iter):
        new_P = []
        for i in range(args.popsize):
            # Select two best parents
            p1 = P.pop(P.index(max(evals)))
            evals.pop(evals.index(max(evals)))
            p2 = P.pop(P.index(max(evals)))
            evals.pop(evals.index(max(evals)))
            # Crossover using mean
            d1,d2 = crossover(p1,p2)
            # Mutation using Gaussian noise
            new_P.append(d1)
            new_P.append(d2)
        
        P = new_P
        evals = []
        for p in P:
            evals.append((fitness(p.evaluate(data_train),p)))
        #find the best while size < elitism ??
        if iter % 2000 == 0:
            print(f'[Train error @{iter}]: {max(evals)}')



if __name__ == '__main__':
    main()