# Call me

Call the `call_me()` function by first overflowing the buffer with `128` bytes and then calling the `ret` gadget and the address of the `call_me()` function using the `32bit calling convention`.

[Solution Code](./sol.py)

> Flag : HZ2018{ROP_ROP_ROP_ROP_42a27134b6f7e73c}