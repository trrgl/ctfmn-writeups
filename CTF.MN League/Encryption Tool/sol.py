import argparse
import sys
from typing import Optional, Tuple

def fnv1a_32(data: bytes) -> int:
    h = 0x811c9dc5
    for b in data:
        h = (h ^ b) * 0x01000193
        h &= 0xffffffff
    return h

def rc4_like_decrypt(key: bytes, data: bytes) -> bytes:
    """KSA + PRGA, matching the C version (bytes indexed 0..255)."""
    assert 1 <= len(key) <= 256
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) & 0xff
        S[i], S[j] = S[j], S[i]
    i = 0
    j = 0
    out = bytearray(len(data))
    for k in range(len(data)):
        i = (i + 1) & 0xff
        j = (j + S[i]) & 0xff
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) & 0xff
        ks = S[t]
        out[k] = data[k] ^ ks
    return bytes(out)

def parse_hex_input(hextext: str) -> bytes:
    clean = hextext.replace(',', ' ').replace('\n', ' ').strip()
    parts = [p for p in clean.split() if p]
    if len(parts) == 0:
        return b''
    if len(parts) == 1 and all(c in '0123456789abcdefABCDEF' for c in parts[0]) and len(parts[0]) % 2 == 0:
        return bytes.fromhex(parts[0])
    return bytes(int(x, 16) for x in parts)

def try_decrypt_with_fnv(challenge = b"challenge") -> bytes:
    hv = fnv1a_32(challenge)
    key = bytes([(hv >> (8*i)) & 0xff for i in range(4)])
    print(f"[+] Using FNV-1a('challenge') = 0x{hv:08X}, key = {key.hex()}") 
    return key

def brute_force_range(cipher: bytes, start: int, end: int, known_plain_prefix: Optional[bytes]=None) -> Optional[Tuple[int, bytes]]:
    cipher_len = len(cipher)
    for val in range(start, end):
        key = bytes([(val >> (8*i)) & 0xff for i in range(4)])
        pt = rc4_like_decrypt(key, cipher)
        if known_plain_prefix is None or pt.startswith(known_plain_prefix):
            return val, pt
    return None

def main():
    ap = argparse.ArgumentParser(description="Decrypt pasta RC4-like ciphertext")
    ap.add_argument("--hex", "-x", help="Ciphertext as hex string (e.g. 'DE AD BE EF' or 'DEADBEEF')")
    ap.add_argument("--infile", "-i", help="Raw ciphertext file (binary)")
    ap.add_argument("--outfile", "-o", help="Write decrypted output to file (default stdout)")
    ap.add_argument("--use-fnv", action="store_true", help="Use FNV-1a('challenge') 4-byte key (default)")
    ap.add_argument("--key", help="Specify 4-byte key as hex (e.g. 01020304) to use instead of fnv")
    ap.add_argument("--brute-start", type=int, default=None, help="Brute-force start integer (inclusive) for 4-byte key")
    ap.add_argument("--brute-end", type=int, default=None, help="Brute-force end integer (exclusive) for 4-byte key")
    ap.add_argument("--known-plain-hex", help="Known plaintext prefix (hex) to validate during brute force")
    args = ap.parse_args()

    if not args.hex and not args.infile:
        print("Provide --hex or --infile. See --help.", file=sys.stderr)
        sys.exit(2)

    if args.hex:
        cipher = parse_hex_input(args.hex)
    else:
        with open(args.infile, "rb") as f:
            cipher = f.read()

    if args.key:
        keybytes = bytes.fromhex(args.key)
        if len(keybytes) != 4:
            print("Key must be 4 bytes (8 hex chars).", file=sys.stderr)
            sys.exit(2)
        print(f"[+] Using explicit key {keybytes.hex()}")
        plain = rc4_like_decrypt(keybytes, cipher)
    elif args.brute_start is not None and args.brute_end is not None:
        kp = bytes.fromhex(args.known_plain_hex) if args.known_plain_hex else None
        print(f"[+] Brute-forcing integers in [{args.brute_start}, {args.brute_end})")
        res = brute_force_range(cipher, args.brute_start, args.brute_end, known_plain_prefix=kp)
        if res is None:
            print("[-] No key found in the given range.")
            sys.exit(1)
        val, plain = res
        keybytes = bytes([(val >> (8*i)) & 0xff for i in range(4)])
        print(f"[+] Found key int=0x{val:08X} -> key={keybytes.hex()}")
    else:
        keybytes = try_decrypt_with_fnv(b"challenge")
        plain = rc4_like_decrypt(keybytes, cipher)

    if args.outfile:
        with open(args.outfile, "wb") as f:
            f.write(plain)
        print(f"[+] Wrote {len(plain)} bytes to {args.outfile}")
    else:
        try:
            sys.stdout.buffer.write(plain)
        except Exception:
            print(plain.hex())

if __name__ == "__main__":
    main()

# Usage python3 sol.py --hex "HEX" > pt.bin
# Flag > CTFMN{F1x3d_Str3am_Bytes_are_n0t_S3cure}