import os
import sys
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256, HMAC
from Crypto.Protocol.KDF import PBKDF2

#ideja: masterpassword za kdf kljuc?
#kako cu cuvati masterpassword?
#cemu moze pristupiti napadac?
#sha za hashiranje
#mac za integritet
#pbkdf2 za kljucž
#iv?

def initIVSalt():
    iv = Random.get_random_bytes(AES.block_size)
    salt = Random.get_random_bytes(16)
    return iv, salt

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
            file.write("")

    myMap = {} 
    iv = salt = ""

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
            if os.path.getsize(path) == 0:
                print("There are no stored passwords.")
                continue
            print("Are you sure you want to reset all stored passwords? (Y/N)")
            answer = input()
            if answer == "Y" or answer == "y":
                with open(path, 'w') as file:
                    file.write('') #clear the file
                print("All stored passwords have been deleted.")
            else:
                print("Operation canceled.")
        elif args[0] == "init":
            if len(args) != 2:
                print("Invalid number of arguments.")
                continue
            mp = args[1] #master password
            #provjeri da li je vec inicijaliziran????
            #vjerojatno samo overwriteaj
            #generiraj stvari idk
            iv, salt = initIVSalt()
            key = PBKDF2(mp, salt, dkLen=32)

            with open(path, 'r') as file:
                file.write("iv: " + iv + "\n")
                file.write("salt: " + salt + "\n")

        elif args[0] == "put":
            if len(args) != 4:
                print("Invalid number of arguments.")
                continue
            mp = args[1]
            if True: #check if mp is correct    
                pass
            if iv == "": #vjv krivo(mozda ne), treba zamjenit sa provjerom mp
                print("Master password has not been initialized.")
                continue    
            
#=========================================================================            
    print("Exiting the program.")

if "__main__" == __name__:
    main()