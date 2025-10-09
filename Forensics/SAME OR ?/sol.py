with open('pool1.txt', 'r') as f:
    data1 = f.read()

with open('pool2.txt', 'r') as f:
    data2 = f.read()

for i,_ in enumerate(data1):
    if data1[i] != data2[i % len(data2)]:
        print(data2[i % len(data2)], end="")

# OUTPUT : HZU18{super_duper_dipe_differ_ox000}