enc = 'HumanOrcHumanHumanOrcHumanHumanHumanHumanOrcHumanOrcOrcHumanOrcHumanHumanOrcHumanOrcHumanOrcHumanOrcHumanHumanOrcOrcHumanHumanHumanOrcHumanHumanOrcOrcOrcHumanHumanHumanHumanOrcOrcOrcOrcHumanOrcOrcHumanOrcHumanHumanOrcHumanOrcHumanHumanOrcOrcOrcHumanOrcHumanOrcHumanOrcOrcOrcHumanHumanOrcOrcHumanOrcOrcOrcHumanOrcHumanHumanHumanOrcHumanOrcOrcOrcOrcOrcHumanOrcHumanOrcHumanHumanOrcHumanHumanOrcOrcHumanHumanOrcHumanOrcHumanOrcOrcOrcHumanHumanHumanHumanHumanOrcOrcHumanOrcOrcHumanHumanHumanOrcOrcHumanHumanHumanHumanOrcHumanOrcOrcHumanHumanHumanOrcOrcHumanOrcOrcHumanHumanOrcHumanOrcHumanOrcOrcOrcOrcOrcHumanOrc'

enc = enc.replace('Human', '0')
enc = enc.replace('Orc', '1')

flag = ""
for i in range(0, len(enc), 8):
    flag += chr(int(enc[i:i+8], 2))

print(flag)

# OUTPUT : HZU18{Just_Replace}