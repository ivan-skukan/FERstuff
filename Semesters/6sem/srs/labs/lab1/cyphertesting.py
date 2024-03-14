from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = b'0123456789012345'

iv = get_random_bytes(AES.block_size)  
aes = AES.new(key, AES.MODE_CFB, iv=iv)

msg = b'This is a secret message'

ciphertext = aes.encrypt(msg)

print(ciphertext)

aesdecrypt = AES.new(key, AES.MODE_CFB, iv=iv)

plaintext = aesdecrypt.decrypt(ciphertext)

print(plaintext.decode('utf-8'))