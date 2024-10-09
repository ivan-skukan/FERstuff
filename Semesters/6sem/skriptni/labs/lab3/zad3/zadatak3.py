import sys
import os
import re

def main():
    if len(sys.argv) != 2:
        print("Usage: python zadatak3.py <path_to_folder>")
        return

    os.chdir(sys.argv[1])

    students = {}
    lab_grades = {}
    with open("studenti.txt", 'r') as f:
        for line in f:
            jmbag,lname,fname = line.split()
            students[jmbag] = (lname,fname)
            lab_grades[jmbag] = {}

    max_lab = 0
    #print(students)
    for filename in os.listdir():
        match = re.match(r'Lab_(\d{2})_g(\d{2})\.txt', filename)
        if match:
            #print(filename)
            with open(filename, 'r') as f:
                for line in f:
                    lab, group = match.groups()
                    #print(group, lab)
                    max_lab = max(max_lab, int(lab))
                    lab = int(lab)
                    #print(lab)
                    jmbag, grade = line.split()
                    lname, fname = students[jmbag]
                    if lab_grades[jmbag].get(lab, None) is not None:
                        print(f"Student {lname} {fname} already has a grade for lab {lab}!")
                        continue
                    #print('here')
                    lab_grades[jmbag][lab] = grade
    #print(lab_grades)
    print("JMBAG".ljust(10), "Prezime".ljust(15), "Ime".ljust(15), end="")
    for i in range(1, max_lab + 1):
        print(f"L{i}".ljust(10), end="")
    print()

    for jmbag in students:
        lname, fname = students[jmbag]
        print(jmbag.ljust(10), lname.ljust(15), fname.ljust(15), end="")
        for i in range(1, max_lab + 1):
            #print(lab_grades[jmbag][i], 'broooo ',end="")
            #print(lab_grades[jmbag].get(i, '-').ljust(10), end="")
            if lab_grades[jmbag].get(i, None) is not None:
                print(lab_grades[jmbag][i].ljust(10), end="")
            else:
                print('-'.ljust(10), end="")
        print()


if __name__ == '__main__':
    main()