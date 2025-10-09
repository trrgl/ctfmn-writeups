enc = "y0u_unl03hT_d3kcBSj!d30g_0k_p0_!"

var1 = [""] * 32

for i in range(31, 16, -2):
    var1[i] = enc[i]
for i in range(16, 32, 2):
    var1[46 - i] = enc[i]
for i in range(8, 16):
    var1[23 - i] = enc[i]
for i in range(0, 8):
    var1[i] = enc[i]

print("HZ{" + "".join(var1) + "}")

# OUTPUT : HZ{y0u_unl0ck3d_Th3_Sp!k3_g00d_j0B!}