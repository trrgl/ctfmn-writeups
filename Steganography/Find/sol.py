import base64

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567=" # BASE32 ALPHABET

enc = """INXW4sZ3SMFdsg2HUIBkjOlFYFvAUnQnrJANByQWG23FOoIQGIp3u3FOMQGqM33SEBWcG65TFEnB3WQYLfUEBXrXI2DFtOJZS
A53POVdWGddIdIfbDmON52,CAZDndPEbBvTG64pRAiNVuXW4ewZLZqFYeQAUgCT/IPJ.5TAY'ZUMRS;TGZJoTMYZDIuZDGolGFlRGGmNRX
MM4DCZgjJklXG;;EYDAsOJRerHBfSWIdhM3h5BI======"""

flag = ""
for i in enc:
    if i in alpha:
        flag += i

print(base64.b32decode(flag).decode())

# OUTPUT : 
# Congratz ..

# A hacker does for love what others would not do for money.

# hz{0c4de3e3f24df1bc67c81e7100918ed3}

# FLAG : hz{0c4de3e3f24df1bc67c81e7100918ed3}
