# ugugdsun C hel deerh code iin check_flag() function-g esergeern bichne

enc = [72, 91, 87, 50, 60, 126, 84, 52, 126, 108, 120, 88, 63, 82, 63, 124, 79, 87, 103, 125, 75, 93, 37, 127, 43, 100] # encrypted flag
flag = ""
for i in range(len(enc)):
    flag += chr(enc[i] ^ i) # Bitwise XOR Gate ees garj bui utgiig ASCII Code iin daguur temdegt bolgon huvirgana

print(flag)

# OUTPUT : HZU18{R3verS3_1s_Fun_H3h3}