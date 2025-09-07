# hasah too biced flag aa nuguu talaasn unshij bolno
enc = [619, 627, 629, 626, 613, 626, 608, 605, 615, 628, 533, 633, 639, 534, 627, 633, 625, 530, 596, 587, 533, 610, 633, 627, 598, 537, 526, 632, 633, 632, 527, 603]
key = sum([c for c in b'MUSTCTF'])
flag = ''
for i in enc:
    flag += chr(i ^ key)

print(flag)

# OUTPUT : MUSTCTF{AR3_Y0U_W4rm3D_Up?(^_^)}