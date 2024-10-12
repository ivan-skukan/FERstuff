import sys

def get_dimensions(matrix):
    i = j = 0

    while True:
        if not (i,j) in matrix:
            break
        j += 1
    while True:
        if not (i,0) in matrix:
            break
        i += 1
    #print(i,j)
    return i, j

def multiply_matrix(A,B,result_file):
    n_A, m_A = get_dimensions(A)
    n_B, m_B = get_dimensions(B)

    if m_A != n_B:
        print('Matrices cannot be multiplied')
        return
    
    AB = {}

    for i in range(n_A):
        for j in range(m_B):
            sum = 0
            for k in range(m_A):
                sum += A[(i,k)] * B[(k,j)]
            AB[(i,j)] = sum

    with open(result_file, 'w') as f:
        f.write('A*B:\n')
        f.write(f"{n_A} {m_B}\n")
        for i in range(n_A):
            for j in range(m_B):
                if AB[(i,j)] != 0:
                    f.write(f"{i} {j} {AB[(i,j)]}")
                    f.write('\n')
            #f.write('\n')            

    return AB

def print_matrix(matrix,name):
    matrix = dict(sorted(matrix.items()))
    print(name,':')

    i = 0
    while True:
        j = 0
        print('   ',end = '')
        while True:
            if (i, j) in matrix:
                print("{:5.2f}".format(matrix[(i, j)]), end=' ')
                j += 1
            else:
                break
        print() 
        if (i + 1, 0) not in matrix:  
            break
        i += 1

def read_file(file):
    A = {}
    B = {}

    with open(file, 'r') as f:
        n, m = map(int, f.readline().split())

        line = f.readline().strip()
        while line:
            row, col, val = map(int, line.split())
            A[(row, col)] = val
            line = f.readline().strip()
        
        for i in range(n):
            for j in range(m):
                if (i,j) not in A:
                    A[(i,j)] = 0

        n, m = map(int, f.readline().split())
        line = f.readline().strip()
        while line:
            row, col, val = map(int, line.split())
            B[(row, col)] = val
            line = f.readline().strip()

        for i in range(n):
            for j in range(m):
                if (i,j) not in B:
                    B[(i,j)] = 0

    return A,B        

def main():
    file = sys.argv[1]
    result_file = sys.argv[2]

    A,B = read_file(file)

    print_matrix(A,'A')
    print_matrix(B,'B')
    #exit()
    AB = multiply_matrix(A,B,result_file)
    print_matrix(AB,'A*B')


if __name__ == '__main__':
    main()