from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256, HMAC, SHA1
import base64
"""
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

hmac = HMAC.new(key, digestmod=SHA256)
hmac.update(msg)
print(hmac.hexdigest())
encrypt = aes.encrypt_and_digest(msg)
"""

iv = Random.get_random_bytes(AES.block_size)
print(iv) 
print(str(iv))

key = b'0123456789012345'
msg = "message".encode('utf-8')

aes = AES.new(key, AES.MODE_GCM,  nonce=iv)

ciphertext, tag = aes.encrypt_and_digest(msg)

#print(ciphertext)

aesdecrypt = AES.new(key, AES.MODE_GCM, nonce=iv)

decrypt = aesdecrypt.decrypt_and_verify(ciphertext, tag)

#print(decrypt.decode('utf-8'))

with open('test.txt', 'w') as file:
    #file.write(ciphertext.)
    pass

print()
iv = base64.b64encode(iv).decode('utf-8')
print(iv)
line = base64.b64encode(b'|').decode('utf-8')
big = iv + '|' + iv

iv = big.split('|')[0]
iv = base64.b64decode(iv)
print(iv)

