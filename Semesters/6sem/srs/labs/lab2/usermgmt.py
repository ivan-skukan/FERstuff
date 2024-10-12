import sys
import os
import bcrypt
from getpass import getpass

def checkPassValidity(pw):
    if len(pw) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if pw.isalpha():
        print("Password must contain at least one number.")
        return False
    if pw.isdigit():
        print("Password must contain at least one letter.")
        return False
    if pw.islower() or pw.isupper():
        print("Password must contain both upper and lower case letters.")
        return False
    return True

def readDict(path):
    if not os.path.exists(path) or os.stat(path).st_size == 0:
        return {}
    with open(path, 'r') as file:
        mydict = {}
        for line in file:
            mydict[line.split(' ')[0]] = line.split(' ')[2]
        return mydict

def getNewSalt():
    return bcrypt.gensalt()

def main():
    args = sys.argv[1:]
    path = 'user_base.txt'
    forcePassDict = readDict(path)
    #salt = readSalt(path) if os.path.exists(path) else getNewSalt()
    
    if len(args) < 1:
        print("Usage: python manager.py <command> <args>\nor ./manager.py <command> <args>")
        return
    #add user
    if args[0] == 'add':
        if len(args) != 2:
            print("Usage: python manager.py add <username>")
            exit(1)

        user = args[1]
        if user in forcePassDict:
            print("Something went wrong.")
            exit(1)
        pw = getpass("Password: ")
        if not checkPassValidity(pw):
            exit(1)
        pwcheck = getpass("Password (again): ")
        if pw != pwcheck:
            print("Passwords do not match.")
            exit(1)
        salt = getNewSalt()
        if not os.path.exists(path) or os.stat(path).st_size == 0:
            with open(path, 'w') as file:
                hashPass = bcrypt.hashpw(pw.encode(), salt)
                hashpass_string = hashPass.decode('utf-8')
                salt_string = salt.decode('utf-8')
                file.write(args[1] + ' ' + hashpass_string + ' 0 ' + salt_string)
        else:
            with open(path, 'a') as file:
                hashPass = bcrypt.hashpw(pw.encode(), salt)
                hashpass_string = hashPass.decode('utf-8')
                salt_string = salt.decode('utf-8')
                file.write('\n' + args[1] + ' ' + hashpass_string + ' 0 ' + salt_string)        
    #change pass for user
    if args[0] == 'passwd':
        if len(args) != 2:
            print("Usage: python manager.py passwd <username>")
            exit(1)
        if not os.path.exists(path):
            print("No users have been added.")
            exit(1) 

        user = pw = salt = None
        userFound = False
        with open(path, 'r+') as file:
            for line in file:
                user, pw, _, salt = line.strip().split(' ')
                if user == args[1]:
                    userFound = True
                    break
        if not userFound:
            print("Something went wrong.")
            exit(1)

        newpass = getpass("New password: ")
        if not checkPassValidity(newpass):
            exit(1)
        newpasscheck = getpass("New password (again): ")
        if newpass != newpasscheck:
            print("Passwords do not match.")
            exit(1)
        
        #check if needed
        if bcrypt.hashpw(newpass.encode(), salt.encode()).decode('utf-8') == pw:
            print("New password must be different from the old one.")
            exit(1)        
        
        string = ""
        salt = getNewSalt()
        #hashnewpass = bcrypt.hashpw(newpass.encode(), salt)
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                lineAppend = line.strip()
                if line.split(' ')[0] == user:
                    lineAppend = user + ' ' + bcrypt.hashpw(newpass.encode(), salt).decode('utf-8') + ' ' + line.split(' ')[2] + ' ' + salt.decode('utf-8')
                string += lineAppend + '\n'
        
        with open(path, 'w') as file:
            file.write(string.rstrip())
        return
    #force change pass for user
    if args[0] == 'forcepass':
        if len(args) != 2:
            print("Usage: python manager.py forcepass <username>")
            exit(1)
        if not os.path.exists(path):
            print("No users have been added.")
            exit(1)    

        forcePassDict = readDict(path)
        if args[1] not in forcePassDict:
            print("Something went wrong.")
            exit(1)    
        string = ""
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                lineAppend = line.strip()
                if line.split(' ')[0] == args[1]:
                    lineAppend = line.split(' ')[0] + ' ' + line.split(' ')[1] + ' 1 ' + line.strip().split(' ')[3]
                string += lineAppend + '\n'
        with open(path, 'w') as file:
            file.write(string.rstrip())
    #remove user
    if args[0] == 'del':
        if len(args) != 2:
            print("Usage: python manager.py remove <username>")
            exit(1)
        if not os.path.exists(path) or os.stat(path).st_size == 0:
            print("No users have been added.")
            exit(1)

        forcePassDict = readDict(path)
        if args[1] not in forcePassDict:
            print("Something went wrong.")
            exit(1)

        string = ""
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.split(' ')[0] == args[1]:
                    continue
                string += line.strip() + '\n'
        with open(path, 'w') as file:
            file.write(string.rstrip()) 
        print("User removed.")           

if __name__ == '__main__':
    main()    