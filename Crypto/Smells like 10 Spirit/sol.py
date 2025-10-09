import base64
import codecs

flag = 'RUt1MVpUNGpyR0laWkh5ZUVHQUdGMEkzSDJjbkYwODBwUnVPbnliakFKTVNyVVNZb3pTS0FIRVhGSUVpRlNBWXBSZ3ZaSFNWSTFNbkZKQWZweGdHQVJJSFpKNWhyUlNGRDBwakNEPT0='
for _ in range(5):
    flag = base64.b64decode(flag).decode() # .decode() = byte -> string
    flag = codecs.encode(flag, 'rot_13')

print(flag)

# OUTPUT : HZU18{Hell0_friend_how_Loow?}