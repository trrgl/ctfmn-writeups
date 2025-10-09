with open('readme', 'r') as f:
    lines = f.readlines()

with open('cipher', 'r') as f:
    coords = f.readlines()

for coord in coords:
    x,y = coord.split(', ')
    print(lines[int(x) - 1][int(y) - 1], end="")

# OUTPUT : flag is Wow_How_much_time_did_you_spend_?_Anyway_you_are_good.
# FLAG : HZU18{Wow_How_much_time_did_you_spend_?_Anyway_you_are_good.}