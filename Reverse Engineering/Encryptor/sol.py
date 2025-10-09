kxor=[1, 218, 209, 78, 85, 100, 24, 166, 228, 58, 113, 11, 68, 5, 94, 33, 87, 114, 144, 118, 64, 51, 228, 152, 13, 194, 47, 18, 144, 96]
enc=[140, 129, 94, 174, 35, 74, 47, 143, 47, 174, 39, 73, 16, 51, 120, 41, 85, 119, 145, 213, 105, 16, 191, 60, 217, 131, 178, 28, 255, 250]
key=[196]

for i in range(1, len(kxor)):
    tulhuur = 1
    for j in range(1, i):
        tulhuur ^= key[j]
    tulhuur ^= kxor[i]
    key.append(tulhuur)

for i in range(len(enc)):
    print(chr(enc[i] ^ key[i]), end='')

# FLAG : HZU18{S1mpl3_r#V#Rs3_ch@LL_!}``