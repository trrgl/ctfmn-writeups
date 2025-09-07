import hashlib
import re
from requests import Session

def md5_int(num):
    return hashlib.md5(str(num).encode()).hexdigest()

lookup = {md5_int(i): i for i in range(100000)}
session = Session()
r = session.get("http://139.162.5.230:10287")
hashes = re.findall(r"[0-9a-f]{32}", r.text)
nums = [lookup[h] for h in hashes]
a, b, c, d, e = nums
answer = a * b + c - (d + e)
r = session.post("http://139.162.5.230:10287/sum", data={"sum": str(answer)})
print(r.text)