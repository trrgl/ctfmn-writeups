import os

files = [f for f in os.listdir('./chall') if os.path.isfile(os.path.join('./chall', f))]

with open(f'chall/838289', 'rb') as f:
    header = f.read()

print(header[:32])
files = sorted(files)
for i,fname in enumerate(files):
    with open(f'output/img{fname}.png', 'wb') as outf:
        with open(f'chall/{fname}', 'rb') as inf:
            outf.write(header + inf.read())

# NOTE : holboh zurga bolgonoo 1, 1 eern shalgana shu.
# FLAG : ccsCTF{zaza_zvgeer_flagaa_aw2}