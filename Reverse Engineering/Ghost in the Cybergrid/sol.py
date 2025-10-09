with open('secret.bin', 'rb') as f:
    enc = f.read()

key = [0x78, 0x56, 0x37, 0x13][::-1]

for i,_ in enumerate(enc):
    print(chr(key[i%4] ^ _), end="")

# OUTPUT : MUSTCTF{SP3CT3R_S335_@LL}