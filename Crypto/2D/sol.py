s = '0anyt1h0in0g1emb0arr0as0s0ing1hi0dden1int1hem0i1dd0leo0ftex1tAll0the1Lore0mIps1um0gene1r0ato0rson1th1eIn0ter0nett0end1tor0e0pea1tp1rede1fin0ed0ch0u0nk1sasn1e1ces1s0arym1akin1gt0h1ist1he1firs0ttru0egen0erat0o0ro0n1the1Int0er0net0It0us0e0sa1dict1ion0a0ryo0fo1verL0atin1word1sco1mbi0ne0dwi1t1hah0and0fulo1f1mo0del0se0nten0cest0ruct1ure1s0to1g1en1era0teLo0re0mIps1umwh1ich0look0sr1easo1nab0le1T1h0egen0era1te0dLo0r0e1m0I1p1s1u1m1is0th1ere1fore0al0w0ays1f0ree0f0rom1r1e0p0etit0ioni1n0ject1edhu1m0ou1rorn1o1n0cha0ract0er1isti1cwor0ds1etct0an0y0th1inge1mb1arra0ssin0g1hid0de0n1i1n1them1iddl0eoft0e1x0t0Allt1heLo1re0mI0ps0um1g0en0e1r1a0tor0s1ont0he0Inte1rne1tt1end1t1ore0peat1pr'
filter = ''

for i in s:
    if i == '0' or i == '1': # zuvhun 0,1 iig salgaj avad
        filter += i

byte_list = [filter[i:i+8] for i in range(0, len(filter), 8)] # 8,8aarn byte bolgood
flag = ''.join([chr(int(b, 2)) for b in byte_list]) # byte uuda text bolgono

print(flag)
# OUTPUT : HZU18{p01s0n3d_b1n4ry12}