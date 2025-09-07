zuv_arr = [247, 211, 219, 121, 251, 56, 255, 105, 158, 146, 93, 89, 89, 56, 186]
oruulsan_arr = []

for a,target in enumerate(zuv_arr):
    print(f'Char {a} :', end=" ")
    for i in range(32, 128):
        if target == (((i << 4) | (i >> 2)) ^ 101) & 255:
            print(chr(i), end= " ")
    print()

# OUTPUT :
# Char 0 : H I
# Char 1 : Z [
# Char 2 : ; z {
# Char 3 : 1 p q
# Char 4 : 9 x y
# Char 5 : 5 t u
# Char 6 : ) h i
# Char 7 : 0
# Char 8 : / n o
# Char 9 : ^ _
# Char 10 : # b c
# Char 11 : 3 r s
# Char 12 : 3 r s
# Char 13 : 5 t u
# Char 14 : = | }

# flag : HZ{pyth0n_b335}