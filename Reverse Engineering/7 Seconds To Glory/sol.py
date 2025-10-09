enc = [0x11, 0x10, 0x17, 0x14, 0x1C, 0x1D, 0x16, 0x19]
for _ in enc:
    print(chr(_ ^ 0x25), end="")

# ┌──(trgl㉿trgl)-[~/Downloads]
# └─$ ./bomb
# 💀 Bomb teserlee hurdan salgaachee: 4521983
# 🔥 Bomb amjilttai sallaa
# ✅ Flag: HZU18{th3_bOmb_h@$_b33n_DefUs3d}