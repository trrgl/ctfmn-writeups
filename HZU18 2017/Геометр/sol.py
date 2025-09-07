with open('input.txt', 'r') as f:
    lines = f.readlines()

flag = ""
for line in lines:
    arr = line.split()
    d = 0
    for i in range(1, len(arr)):
        if int(arr[i-1], 10) != 0:
            if d == 0:
                d = int(arr[i], 10) / int(arr[i-1], 10)
            else:
                if int(arr[i], 10) / int(arr[i-1], 10) == d:
                    if int(arr[i], 10) + 1 >= len(arr):
                        flag += str(int(d))
print('HZU18{' + flag + '}')
# OUTPUT : HZU18{222}