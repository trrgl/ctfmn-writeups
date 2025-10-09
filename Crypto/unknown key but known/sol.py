from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
import os

KNOWN_PART = b"__p4ssw0rd_is_"
enc = long_to_bytes(0xbde9f71794fd5f623456ceff5c37c85a8473a6e92f4cedeb3c5be4d89c1429bbdc169ae6b78814b93cbdca9ef5f4f935)

def encrypt(plaintext):
    unknown_part = os.urandom(2)
    key = KNOWN_PART + unknown_part
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, AES.block_size)).hex()

def decrypt(enc, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(enc)

for i in range(256):
    for j in range(256):
        key = KNOWN_PART + long_to_bytes(i) + long_to_bytes(j)
        flag = decrypt(enc, key)
        if b'HZU18{' in flag:
            print(flag) 
            break

# OUTPUT : HZU18{979fd1aa64c9168b4338c8ae13590498}