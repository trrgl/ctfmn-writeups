# Character bolgong too bolgood, reversedeed, encrypted teige shalgaj bn
enc = '0731733335815479913312380878912235793881848827220866293701370535'[::-1]
toli = {
    'A': 33,
    'B': 45,
    'C': 21,
    'D': 13,
    'E': 18,
    'F': 67,
    'G': 87,
    'H': 53,
    'I': 22,
    'J': 91,
    'K': 98,
    'L': 48,
    'M': 72,
    'N': 19,
    'O': 42,
    'P': 88,
    'Q': 24,
    'R': 37,
    'S': 80,
    'T': 97,
    'U': 63,
    'V': 71,
    'W': 28,
    'X': 54,
    'Y': 16,
    'Z': 50,
    '{': 66,
    '2': 73,
    '_': 83,
    '1': 56,
    '}': 70,
    '0': 10,
    '6': 62,
    '7': 23,
    '8': 44,
    '9': 60,
    '5': 28,
    '4': 30,
    '3': 92
}
reversed_toli = {too: char for char, too in toli.items()}
for i in range(0, len(enc), 2):
    print(reversed_toli[int(enc[i:i+2], 10)], end="")

# OUTPUT : HZ2023{SIMPLE_THINGS_CANTBEHARD}