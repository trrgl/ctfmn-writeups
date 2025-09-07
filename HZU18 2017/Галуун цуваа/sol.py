with open('input.txt', 'r') as f:
    lines = f.readlines()

first_nums = []

for line in lines:
    nums = list(map(int, line.split()))
    if len(nums) < 3:
        continue
    ok = True
    for i in range(2, len(nums)):
        if nums[i] != nums[i-1] + nums[i-2]:
            ok = False
            break
    if ok:
        first_nums.append(str(nums[0]))

flag = f"HZU18{{{''.join(first_nums)}}}"
print(flag)

# OUTPUT : HZU18{1001201021}