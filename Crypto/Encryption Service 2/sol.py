from pwn import *

context.update(arch='i386')
exe = './path/to/binary'

host = args.HOST or '139.59.230.119'
port = int(args.PORT or 10343)


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

flag = b'CTFMN{'
payload_test = b''
payload = b'AA'
count = 0

io = start()
while True:
    if payload == b'':
        payload = b'AAAAAAAA'
        count += 1
    else:
        payload = b'A' * (len(payload) - 1)
    payload_test = flag[-7:]
    while len(payload_test) < 7:
        payload_test = b'A' + payload_test
    begin = count * 32
    end = begin + 32
    io.recvuntil(b'plaintext = ')
    print('[+] Sent :', payload + flag)
    io.sendline(payload)
    io.recvuntil(b'ciphertext = ')
    target = io.recvline()[begin:end]
    print(target)
    for i in range(33, 128):
        io.recvuntil(b'plaintext = ')
        print('[+] Sending :', payload_test + chr(i).encode())
        io.sendline(payload_test + chr(i).encode())
        io.recvuntil(b'ciphertext = ')
        if target == io.recvline()[:32]:
            flag += chr(i).encode()
            print(payload_test + chr(i).encode())
            break
    if chr(flag[-1]) == '}':
        print('[+] FLAG :', flag)
        break
io.interactive()

# FLAG : CTFMN{0racl3_4ttack_0n_3CB}