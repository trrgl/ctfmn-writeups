from pwn import *

context.update(arch='i386')
exe = './path/to/binary'

host = args.HOST or '139.162.5.230'
port = int(args.PORT or 10093)


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

flag = b'HZU18{0racl3_4t'
payload_test = b''
payload = b'A'
count = 0

io = start()
while True:
    if payload == b'A':
        payload = b'AAAAAAAAAAAAAAAA'
        count += 1
    else:
        payload = b'A' * (len(payload) - 1)
    payload_test = flag[-15:]
    while len(payload_test) < 15:
        payload_test = b'A' + payload_test
    begin = count * 32
    end = begin + 32
    io.recvuntil(b'give me message : ')
    print('[+] Sent :', payload + flag)
    io.sendline(payload)
    io.recvuntil(b'encrypted message : ')
    target = io.recvline()[begin:end]
    print(target)
    for i in range(33, 128):
        io.recvuntil(b'give me message : ')
        print('[+] Sending :', payload_test + chr(i).encode())
        io.sendline(payload_test + chr(i).encode())
        io.recvuntil(b'encrypted message : ')
        if target == io.recvline()[:32]:
            flag += chr(i).encode()
            print(payload_test + chr(i).encode())
            break
    if chr(flag[-1]) == '}':
        print('[+] FLAG :', flag)
        break
io.interactive()