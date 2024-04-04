#!/usr/bin/env python3
import os
import sys
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256, HMAC
from Crypto.Protocol.KDF import PBKDF2
import base64
import string
import binascii
from Crypto.Random import random

def get_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return result_str

def initIVSalt():
    iv = Random.get_random_bytes(AES.block_size)
    salt = Random.get_random_bytes(16)
    return iv, salt

def main():
    path = 'passwords.txt'
    args = sys.argv[1:]
    aes = None
    iv = salt = ""
    
    if args[0] == "init":
        if len(args) != 2:
            print("Invalid number of arguments.")
            return
        if os.path.exists(path) and not os.path.getsize(path) == 0:
            print("Master password has already been initialized.")
            return
        
        mp = args[1] 
        iv, salt = initIVSalt()

        padding = get_random_string(32).encode('utf-8')
        key = PBKDF2(mp, salt, dkLen=32, count=100000, prf=lambda p,s: HMAC.new(p,s,SHA256).digest())
        aes = AES.new(key, AES.MODE_GCM, nonce=iv)

        encrypted, tag = aes.encrypt_and_digest(padding)
        base64enc = base64.b64encode(encrypted).decode('utf-8')
        base64tag = base64.b64encode(tag).decode('utf-8')

        iv = base64.b64encode(iv).decode('utf-8')
        salt = base64.b64encode(salt).decode('utf-8')

        bigstring = iv + '|' + salt + '|' + base64enc + '|' + base64tag

        with open(path, 'w+') as file:
            file.write(bigstring)


    elif args[0] == "put":
        if len(args) != 4:
            print("Invalid number of arguments.")
            return
        
        mp = args[1]
        site = args[2]
        password = args[3]

        with open(path, 'r') as file:
            try:
                bigstring = file.read()
                iv = bigstring.split('|')[0]
                iv = base64.b64decode(iv) 
                salt = bigstring.split('|')[1]
                salt = base64.b64decode(salt)
                encrypted = bigstring.split('|')[2]
                encrypted = base64.b64decode(encrypted)
                tag = bigstring.split('|')[3]
                tag = base64.b64decode(tag)
            except binascii.Error:
                print("Integrity of the file has been compromised.")
                return

            key = PBKDF2(mp, salt, dkLen=32, count=100000, prf=lambda p,s: HMAC.new(p,s,SHA256).digest())
            aes = AES.new(key, AES.MODE_GCM, nonce=iv)

            try:
                decrypted = aes.decrypt_and_verify(encrypted, tag)
            except ValueError:
                print("Master password is incorrect or integrity of the file has been compromised.")
                return    
            
            decrypted = decrypted.decode('utf-8')

            site += ' '

            if site in decrypted:
                start = decrypted.find(site) + len(site) + 1 
                end = decrypted.find('\t', start)
                if end == -1:
                    end = len(decrypted)
                oldpass = decrypted[start:end] 
                decrypted = decrypted.replace(site + " " + oldpass, site + " " + password)
                
            else:
                decrypted += "\t" + site + " " + password
            
            #print(decrypted)
            #base64enc = base64.b64encode(encrypted).decode('utf-8')
            #base64tag = base64.b64encode(tag).decode('utf-8')
            #base64line = base64.b64encode(b'|').decode('utf-8')
            iv, salt = initIVSalt()
            key = PBKDF2(mp, salt, dkLen=32, count=100000, prf=lambda p,s: HMAC.new(p,s,SHA256).digest())
            aes = AES.new(key, AES.MODE_GCM, nonce=iv)
            encrypted, tag = aes.encrypt_and_digest(decrypted.encode('utf-8'))
            #iv = base64.b64encode(b"iv:"+iv).decode('utf-8')
            #salt = base64.b64encode(b"salt:"+salt+b"|").decode('utf-8')

            #bigstring = iv + base64line + salt + base64enc + base64line + base64tag
            bigstring = base64.b64encode(iv).decode('utf-8') + '|' + base64.b64encode(salt).decode('utf-8') + '|' + base64.b64encode(encrypted).decode('utf-8') + '|' + base64.b64encode(tag).decode('utf-8')
            #bigstring = base64.b64encode(bigstring.encode('utf-8')).decode('utf-8')

            with open(path, 'w') as file:
                file.write(bigstring)

    elif args[0] == "get":
        if len(args) != 3:
            print("Invalid number of arguments.")
            return
        mp = args[1]
        site = args[2]

        with open(path,'r') as file:
            try:
                bigstring = file.read()
                iv = bigstring.split('|')[0]
                iv = base64.b64decode(iv)
                salt = bigstring.split('|')[1]
                salt = base64.b64decode(salt)
                encrypted = bigstring.split('|')[2]
                encrypted = base64.b64decode(encrypted)
                tag = bigstring.split('|')[3]
                tag = base64.b64decode(tag)
            except binascii.Error:
                print("Master password incorrect or integrity of the file has been compromised.")    
                return

            key = PBKDF2(mp, salt, dkLen=32, count=100000, prf=lambda p,s: HMAC.new(p,s,SHA256).digest())
            aes = AES.new(key, AES.MODE_GCM, nonce=iv)

            try:
                decrypted = aes.decrypt_and_verify(encrypted, tag)
            except ValueError:
                print("Master password is incorrect or integrity of the file has been compromised.")
                return    
            
            decrypted = decrypted.decode('utf-8')
            #print(decrypted)

            site += ' '

            if site in decrypted:
                start = decrypted.find(site) + len(site) + 1
                end = decrypted.find('\t', start)
                if end == -1:
                    end = len(decrypted)    
                password = decrypted[start:end]
                print(password)
            else:
                print("Master password incorrect or integrity of the file has been compromised.")
    else:
        print("Invalid command.")

if "__main__" == __name__:
        main()