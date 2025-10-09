from requests import *
import re
session = Session()

url = 'http://139.162.5.230:10325/'
id = ''
while True:
    print("Sending request to :", url + id)
    r = session.get(url + id)
    print("Response :", r.text)
    id = 'id/'
    match = re.search(r'/id/([0-9a-f-]{36})', r.text)
    if match:
        uuid = match.group(1)
        id += uuid

# FLAG : hz{yeaa_finally_u_got_it_5020311c58d7fb6f}