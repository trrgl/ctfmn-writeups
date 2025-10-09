enc = '6 12 1 7 9 19 19 5 3 18 5 20 19 1 18 5 8 9 4 4 5 14 9 14 20 8 9 19 12 9 19 20'.split(' ')
for _ in enc:
    print(chr(int(_, 10) + 96), end="")

# OUTPUT : flagissecretsarehiddeninthislist
# FLAG : HZU18{secrets_are_hidden_in_this_list}