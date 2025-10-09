# Inside

Decompiling the `ELF binary` using programs like [IDA](https://hex-rays.com/ida-free) or [Ghidra](http://ghidra.net/) will give you a code that:

    1. Asks for a input
    2. Creates a value by XORing matching indexed elements in arrays "ratata" and "matata"
    3. Checks if the input and the value matches

We have to reverse engineer the value that is being created.

[Solution Code](./sol.py)

> Flag : ccsCTF{debugg1ngg}