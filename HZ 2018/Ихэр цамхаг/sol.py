with open('elf', 'r') as f:
    data1 = f.read()

with open('elf2', 'r') as f:
    data2 = f.read()

for i,_ in enumerate(data1):
    if data1[i] == data2[i] and data1[i] != " ":
        print(data1[i], end="")

# OUTPUT : HZ{jhon_hetsuul_yum}