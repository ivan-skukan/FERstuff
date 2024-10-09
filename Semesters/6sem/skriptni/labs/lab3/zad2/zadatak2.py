import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python zadatak2.py <filename>")
        sys.exit(1)
    print("test")
    filename = sys.argv[1]
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)

    step = 0.1
    table = {}


    for i,line in enumerate(lines):
        key = str(i).zfill(3)
        table[key] = str(key) + '#'
        numbers = line.strip().split()
        numbers.sort()

        for i in range(1,10):
            idx = i * step * len(numbers) - 1
            table[key] += numbers[int(idx)] + '#'
        table[key] = table[key][:-1]

    print("Hyp#Q10#Q20#Q30#Q40#Q50#Q60#Q70#Q80#Q90")
    for key in table:
        print(table[key])
            

if __name__== "__main__":
    main()