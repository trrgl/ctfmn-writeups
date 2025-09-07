offset = 'tfgzn//Czp({C&XCk(nq/xC+L##a'
length = len(offset)

for i in offset:
    print(chr(ord(i) ^ length), end="")