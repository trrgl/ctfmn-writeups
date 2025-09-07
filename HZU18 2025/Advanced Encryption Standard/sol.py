from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes

enc = 0x2ae44c5da2804d2048f5f713f84be44d385ab3527ece6d18f4b90de3455720a78b3a2ed777229975afe99bf1ce57c794
enc = long_to_bytes(enc)

key = sha256(b'HZU18{').digest()
cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(enc)

print(flag)

# OUTPUT : HZU18{AES_1s_st4nd4rd_and_3verywher3}