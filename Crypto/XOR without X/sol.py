def decrypt(keys_hex, cts_hex):
    keys = [bytes.fromhex(k) for k in keys_hex]
    cts = [bytes.fromhex(c) for c in cts_hex]

    length = len(cts[0])
    plaintext = bytearray(length)

    for i in range(length):
        bit_value = 0
        for bit in range(8):
            bit_set = False
            for k, c in zip(keys, cts):
                key_bit = (k[i % len(k)] >> bit) & 1
                ct_bit = (c[i] >> bit) & 1
                if ct_bit == 1 and key_bit == 0:
                    bit_set = True
                    break
            if bit_set:
                bit_value |= (1 << bit)
        plaintext[i] = bit_value

    return bytes(plaintext)

keys_hex = [
    "17f6952587335ca96bb8a7a21283089a8b2653b3",
    "b1e1961ae901ff84d13e7957ae79db389174d60d",
    "6e8bdd2dc1a467b7806904c52d489e85e7208bfe",
    "5f50a5754d473ef4c10703a52586269a3bcda0f8",
    "a3062b37350fa53c325b307f53bb81805044ac73",
    "470fcaf2bc5b278746b5d95cd10d4c9e7dab76f1",
    "79861ba08d10ada9e46285da5dcec03501dad5eb",
    "4602e7701d9e89a487e327b6162b61518ebcbf23",
    "602fd38393c1c75212ac626cd6bbca9604828644",
    "529db8cb736e0e68a4850e4cc50201b009680adc"
]
cts_hex = [
    "7ff7ff65ef737ffb6ffde7ff72eb7cffeb7777ff7ff6f577e7777def6ffbffee7ff37bfbdf367bb737febd35e7737eeb7ffd",
    "fde1fe7bed61fff7ff7f7d5fee79ff7ff977f75ffff1f77ae975ffefff7f7f7fef7bfb79df74fe3fb3f9bf3ae963ffe7f57f",
    "6febff6dede57ff7ef6d65df6f69fef7ef73efff6ffbfd7fe1f46fffee7b5fed6f7bfffdff30fbff7ebbfd3de1e777f7b47d",
    "7f71ff756d677ff7ef6f67ff67ef76ff7bffe5ff7f70e5776d777fffef775fed6ff777fb7ffdf8ff7f78bd756d673ef7f57f",
    "ef677b777d6fff7f7f7f757f73fbf5f77977ed7fef766f77757fed7f7e7b7f7f7ffbf3f95f74fc77b33e3b37756fb77f367f",
    "6f6ffaf3fc7b7ff76ffdfd5ff36d7cff7dfb77ff6f7feff2fd7f6fef6ef7df7cff7f7fff7fbb7ef7773ffbf2fd7b37e776fd",
    "7de77be1ed71fffbef6fe5df7feff47769fbf5ff7ff67ff2ed74edefee73dffe7ffff37d5ffafdff7bbe3bb0ed73bfebf47f",
    "6f63ff717dfffbf7efef67ff766b7577efffff7f6f72e7727dfee9efeff37ffe7f7b7379dfbcff37763aff707dffbfe7b7ff",
    "6d6ffbe3ffe1ff737fed677ff6fbfef76df3e75f6f7ff7f3f3f5ef7f7eff7f6cfffbfbff5fb2fe77723ffbb3f3e3f77336fd",
    "7ffdfaeb7f6f7f7befed6f5fe76b75f7697b6fdf7ffdfdfb737e6f6feef75f6cef7373f95f787aff72bdb9fb736f3e6bb4fd"
]

flag = decrypt(keys_hex, cts_hex)
print(flag.decode())

# OUTPUT : mazala{some_bitwise_operations_lossy_0x72890ac6c4}