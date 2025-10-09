import time

xor = [106, 123, 124, 51, 18, 117, 116, 33, 85, 118, 103, 70, 11, 64, 36, 112, 97, 108, 66, 74, 66, 105, 120, 44, 21, 65, 20, 84, 29, 98, 115, 90, 109, 86, 58, 34]

start_epoch = 1640995200  # Jan 1, 2022
end_epoch = int(time.time())

def random():
    global n
    n = int(((n + 0x4ae7777) * 0x41) % 7123)
    n = (n + 0x325b28043b9b6) ^ 0x586cfc90c5b2
    n = (n * 63) % 0xC1CB7296
    n = n ^ 0x1754F2F
    n = (n*0xFF) % 4394967296
    n = n ^ 0x222F44CB
    n = n | 0x1234167890
    n = ((n + 14351514) * 32) % 7777333
    return int(n % 100)

def try_seed(epoch):
    global n
    n = epoch / 10000

    flag_bytes = []
    for x in xor:
        k = random()
        flag_bytes.append(x ^ k)
    try:
        flag = bytes(flag_bytes).decode()
        if flag.startswith("HZU18{"):
            print(f"Found flag with seed {epoch}: {flag}")
            return True
    except UnicodeDecodeError:
        pass
    return False

for seed in range(start_epoch, end_epoch+1, 10):
    if try_seed(seed):
        break
