import sys
import os
from getpass import getpass
import bcrypt

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
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as file:
        return dict([line.strip().split(' ')[::2] for line in file])

def getNewSalt():
    return bcrypt.gensalt()

def main():
    args = sys.argv[1:]
    path = 'user_base.txt'
    forcePassDict = readDict('user_base.txt')

    if len(args) != 2:
        print("Usage: python login.py login <user>\nor ./manager.py login <user>")
        return
    
    if args[0] == 'login':
        user = args[1]
        savedPass = salt = None

        with open(path, 'r') as file:
            for line in file:
                if user in line:
                    savedPass = line.split(' ')[1].encode()
                    salt = line.strip().split(' ')[3].encode()
                    break 
        if user in forcePassDict:
            checkForceChangePass = forcePassDict[user]
        else:
            print("Something went wrong.")
            return
        if checkForceChangePass == '1':
            oldpasscheck = getpass("Password: ")
            if bcrypt.hashpw(oldpasscheck.encode(), salt) != savedPass:
                print("Username or password wrong.")
                return
            newSalt = getNewSalt()
            newpass = getpass("New Password: ")
            if not checkPassValidity(newpass):
                return
            newpasscheck = getpass("New Password (again): ")

            if newpass != newpasscheck:
                print("Passwords do not match.")
                return
            if bcrypt.hashpw(newpass.encode(), salt) == savedPass:
                print("Password cannot be the same as the old password.")
                return
            
            string = ""
            with open(path, 'r') as file:
                for line in file:
                    lineAppend = line.strip()
                    if user == line.split(' ')[0]:
                        lineAppend = line.split(' ')[0] + ' ' + bcrypt.hashpw(newpass.encode(), newSalt).decode('utf-8') + ' 0 ' + newSalt.decode('utf-8')
                    string += lineAppend + '\n'
            with open(path, 'w') as file:
                file.write(string.rstrip())

            print("Password changed successfully. Logged in.")
            os.system('bash')
            return
        else:
            counter = 0
            while counter < 3:
                pw = getpass("Password: ")
                hashPass = bcrypt.hashpw(pw.encode(), salt)
                if hashPass == savedPass:
                    print("Login successful.")
                    os.system('bash')
                    return
                else:
                    print("Username or password wrong.")
                counter += 1
            return

    else:
        print("Usage: python login.py login <user>\nor ./manager.py login <user>")
        return   

if __name__ == '__main__':
    main()