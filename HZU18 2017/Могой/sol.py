# 1. .pyc decompile hiine.
enc = 'I[V29|S4wfst4s~'
flag = ''
for _ in enc:
    flag += chr(ord(_) - 1)

print(flag)

# OUTPUT : HZU18{R3vers3r}