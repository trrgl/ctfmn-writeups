import base64

enc = "HL13Oe5cEdBUwYlKM0hONdROENJsFNvz"
enc1 = ""
for c in enc:
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        offset = (ord(c) - base - 18) % 26
        if offset < 0: offset += 26
        c = chr(base + offset)
    enc1 += c

enc1 = base64.b64decode(enc1.encode()).decode()[::-1]
enc1 = base64.b64decode(enc1.encode()).decode()

print(enc1)

# OUTPUT : inYOUUURRFLAGggg
# FLAG : MUSTCTF{inYOUUURRFLAGggg}