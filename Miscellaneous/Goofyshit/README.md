# Goofyshit

Split the `.gif` into individual frames using https://ezgif.com/split.

Scanning the QR code on the 4th and the 7th will give us 2 pastebin links:

    https://pastebin.com/RTpHLsFn
    https://pastebin.com/y6kdkmwt

Inside there are two `Base64` encrypted texts.

Joining them together and decrypting will give us the flag.

[CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=WTJOelExUkdlMmN3TUdZeGJqbGZOSEl3ZFc1a2ZRPT0&oeol=FF)

> Flag : ccsCTF{g00f1n9_4r0und}