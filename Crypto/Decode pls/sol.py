# rot13(reverse(flag^"aaaC9911111119"))=="QCOHJJHOKK8LC4"
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

enc = "QCOHJJHOKK8LC4"
enc = codecs.encode(enc, "rot13")[::-1].encode()
enc = bytes_to_long(enc) ^ bytes_to_long(b"aaaC9911111119")
print(long_to_bytes(enc).decode())

# OUTPUT : U18{aasdffdsa}