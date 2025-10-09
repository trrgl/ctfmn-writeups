from pwn import *

context.update(arch='i386')
exe = './path/to/binary'

host = args.HOST or '139.162.5.230'
port = int(args.PORT or 10172)


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

hash1 = set()
hash2 = set()
hash3 = set()
hash4 = set()
hash5 = set()
io = start()
io.clean()
while True:
    if len(hash1) + len(hash2) + len(hash3) + len(hash4) + len(hash5) >= 30: break
    print(len(hash1) + len(hash2) + len(hash3) + len(hash4) + len(hash5))
    io.recvuntil(b'option = ')
    io.sendline(b'sign')
    io.recvuntil(b'Round 1. ')
    hash1.add(io.recvline().strip())
    io.recvuntil(b'Round 2. ')
    hash2.add(io.recvline().strip())
    io.recvuntil(b'Round 3. ')
    hash3.add(io.recvline().strip())
    io.recvuntil(b'Round 4. ')
    hash4.add(io.recvline().strip())
    io.recvuntil(b'Round 5. ')
    hash5.add(io.recvline().strip())
for a in hash1:
    for b in hash2:
        for c in hash3:
            for d in hash4:
                for e in hash5:
                    io.recvuntil(b'option = ')
                    io.sendline(b'verify')
                    io.recvuntil(b'signature = ')
                    io.sendline(a)
                    io.recvuntil(b'letter = ')
                    io.sendline(b'M')
                    io.recvuntil(b'signature = ')
                    io.sendline(b)
                    io.recvuntil(b'letter = ')
                    io.sendline(b'M')
                    io.recvuntil(b'signature = ')
                    io.sendline(c)
                    io.recvuntil(b'letter = ')
                    io.sendline(b'M')
                    io.recvuntil(b'signature = ')
                    io.sendline(d)
                    io.recvuntil(b'letter = ')
                    io.sendline(b'M')
                    io.recvuntil(b'signature = ')
                    io.sendline(e)
                    io.recvuntil(b'letter = ')
                    io.sendline(b'M')
                    print(io.recvline()) # heseg deesh doosho scrolldod harjihguyudo
io.interactive()

