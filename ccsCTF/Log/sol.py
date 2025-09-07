from datetime import datetime

with open("numbers.log", "r") as f:
    log_data = f.readlines()

sorted_logs = sorted(
    [line.strip() for line in log_data if line.strip()],
    key=lambda line: datetime.strptime(line.split(" - ")[0], "%Y-%m-%d %H:%M:%S.%f")
)

with open("sorted.log", "w") as f:
    for entry in sorted_logs:
        f.write(entry + "\n")

# OUTPUT :
# ......
# 2023-01-03 15:46:20.382679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /c - 39950
# 2023-01-03 15:46:20.385679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /c - 6142
# 2023-01-03 15:46:20.388679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /s - 48333
# 2023-01-03 15:46:20.391679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /C - 16796
# 2023-01-03 15:46:20.394679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /T - 45424
# 2023-01-03 15:46:20.397679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /F - 57044
# 2023-01-03 15:46:20.400679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /{ - 56376
# 2023-01-03 15:46:20.403679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /C - 34061
# 2023-01-03 15:46:20.406679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /0 - 18217
# 2023-01-03 15:46:20.409679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /n - 13820
# 2023-01-03 15:46:20.412679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /f - 3610
# 2023-01-03 15:46:20.415679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /u - 43593
# 2023-01-03 15:46:20.418679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /5 - 46224
# 2023-01-03 15:46:20.421679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /1 - 49001
# 2023-01-03 15:46:20.424679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /0 - 5135
# 2023-01-03 15:46:20.427679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /n - 42868
# 2023-01-03 15:46:20.430679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /} - 51928
# 2023-01-03 15:46:20.433679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /1 - 42167
# 2023-01-03 15:46:20.436679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /m - 9672
# 2023-01-03 15:46:20.439679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /3 - 13974
# 2023-01-03 15:46:20.442679 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 - GET /} - 5898

# flag : ccsCTF{C0nfus10n}