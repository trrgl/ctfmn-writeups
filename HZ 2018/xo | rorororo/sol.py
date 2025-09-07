binary = "111000101111000011010001110100101001101011111000111101011110100011000011110001001100101111011000110100111111010111100001100110011101001111010111"

b = bytes(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))

for key in range(256):
    decrypted = bytes(c ^ key for c in b)
    try:
        text = decrypted.decode('utf-8')
        if all(32 <= ord(ch) <= 126 for ch in text) and 'HZ' in text:
            print(text)
    except:
        continue

# OUTPUT : HZ{x0R_Binary_K3y}