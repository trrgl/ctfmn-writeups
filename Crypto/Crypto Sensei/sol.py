from Crypto.Util.Padding import pad

kii = '9769769769769769'.encode()
enc = '3e31303e31303e4b035a0e0f0050560d08025601005558014c7f62746d65627408070608070608070608070608070608'
enc = bytes.fromhex(enc)[::-1]
sub = bytearray()
for i, byte in enumerate(enc):
    kii_byte = kii[i % len(kii)]
    sub.append(byte ^ kii_byte)

print(sub)

# OUTPUT : bytearray(b'1111111111111111MUSTCTF{7ab68a414af988c4}\x07\x07\x07\x07\x07\x07\x07')
# FLAG : MUSTCTF{7ab68a414af988c4}