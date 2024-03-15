from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256, HMAC, SHA1

key = b'0123456789012345'

iv = Random.get_random_bytes(AES.block_size) 

aes = AES.new(key, AES.MODE_CFB, iv=iv)

#msg = b'This is a secret message'
msg = input("Enter a message: ").encode('utf-8')
ciphertext = aes.encrypt(msg)

#print(ciphertext.decode('utf-8')) #whatevuhhhhh

aesdecrypt = AES.new(key, AES.MODE_CFB, iv=iv)

plaintext = aesdecrypt.decrypt(ciphertext)

print(plaintext.decode('utf-8'))