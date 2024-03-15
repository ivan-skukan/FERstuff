import os
import sys
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256, HMAC, SHA1

#ideja: masterpassword za kdf kljuc?
#kako cu cuvati masterpassword?
#cemu moze pristupiti napadac?

def help():
    print("\nCommands:") 
    print("\tinit <master_password> - initializes the master password - required for all other commands related to passwords. Can be called only once.")
    print("\tput <master_password> <service> <password> - adds a new password for a service")
    print("\tget <master_password> <service> - retrieves a password for a service")
    print("\tlist <master_password> - lists all services for which a password is stored") #dodaj ako stignes
    print("\treset - deletes all stored passwords including the master password") 
    print("\texit - exits the program")


def main():
    path = 'passwords.txt'
    #args = sys.argv[1:]

    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.write('Master Password: \n')

    myMap = {} 

    print("\nThe password manager is running. Check docs for more info.")       
    print("Write 'help' for a list of commands.")
    print("Write 'exit' to exit the program.\n")
    while True:
        args = input("Enter command: ").split(" ")
        if args[0] == "exit":
            break
        elif args[0] == "help":
            help()
        elif args[0] == "reset":
            print("Are you sure you want to reset all stored passwords? (Y/N)")
            answer = input()
            if answer == "Y" or answer == "y":
                with open(path, 'w') as file:
                    file.write('Master Password: \n')
                print("All stored passwords have been deleted.")
            else:
                print("Operation canceled.")
        elif args[0] == "init":
            if len(args) != 2:
                print("Invalid number of arguments.")
                continue
            with open(path, 'r+') as file:
                mp = file.readline().split(":")[1].strip() #placeholder, mp se ne sprema 
                #provjeri da li je vec inicijaliziran
            
#=========================================================================            
    print("Exiting the program.")

if "__main__" == __name__:
    main()