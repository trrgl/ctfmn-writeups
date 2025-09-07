import base64

with open('encrypted.txt', 'rb') as f:
    enc = f.read()

enc = enc[2:]
enc = enc[:-1]
while True:
    try:
        enc = base64.b64decode(enc)
        enc = base64.b32decode(enc)
    except Exception as e:
        print(e)
        print(enc)
        input()

# Flag : MUSTCTF{l00p_m4st444}