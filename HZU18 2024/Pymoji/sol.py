# code oo ynzalj bicel bolo :)
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x // y

data = ['3$N7-17-', '-3c69a08', '6-dad6-4', 'LO0K-L1K', '28e8e}', 'HZU18{D0', '3-4-FL4G', '577-8d9b', '-dbc0ac3']

def build_flag():
    result = []
    result.append(data[sub(ord('😎'), ord('😉'))])
    result.append(data[add(ord('😀'), -ord('😀'))])
    result.append(data[int(mul(ord('😑'), 2.34e-5))])
    result.append(data[div(ord('🤐') * 6, ord('🤐'))])
    result.append(data[add(ord('🤓'), mul(ord('🤒'), -1))])
    result.append(data[sub(ord('🤑'), ord('🤏'))])
    result.append(data[-2])
    result.append(data.pop())
    [result.append(x) for x in data if len(x) != 8]
    return result

print(''.join(build_flag()))

# OUTPUT : HZU18{D03$N7-17-LO0K-L1K3-4-FL4G-3c69a086-dad6-4577-8d9b-dbc0ac328e8e}
