import os
import sys

def help():
    print("") #dovrsi

def main():
    path = 'passwords.txt'
    args = sys.argv[1:]

    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.write('')

    myMap = {} 

    print("The password manager is running. Check official documentation for more information.")       
    print("Write 'help' for a list of commands.")
    print("Write 'exit' to exit the program.")
    while True:
        args = input("Enter command: ").split(" ")
        if args[0] == "exit":
            break
        elif args[0] == "help":
            help()
        elif args[0] == "add":
            pass
            
#=========================================================================            
    print("Exiting the program.")

if "__main__" == __name__:
    main()