#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

context.update(arch='i386')
exe = 'sol.py'

host = args.HOST or '139.59.230.119'
port = int(args.PORT or 10327)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

lo = 1
hi = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096

io = start()
io.clean()
io.recvuntil(b':')
while lo <= hi:
    mid = (lo + hi) // 2
    io.sendline(str(mid).encode())
    response = io.recvline().decode(errors='ignore').strip()
    print(response)

    if 'Хэтрээд явчихав уу?' in response:
        hi = mid - 1
    elif 'Арай наана уу?' in response:
        lo = mid + 1
    elif 'HZU18{' in response:
        print("FLAG OLCLO PZDA :", response)
        break
    else:
        print("YU SHAGAD :", response)
        break
io.interactive()

# OUTPUT : HZU18{l@@rgEE_b1n@r33_s3arcH_4bb80b567d0348a9}