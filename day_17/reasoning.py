"""
asm:
    BST A
    BXL 1
    CDV B
    ADV 3
    BXL 4
    BXC
    OUT B
    JNZ 0

pseudocode:
    do:
        B = A % 8
        B ^= 1
        C = A // (2 ** B)
        A //= 8
        B ^= 4
        B ^= C
        print(B % 8)
    while A > 0

simplified pseudocode:
    do:
        p = (A % 8) ^ 1
        q = A // (2 ** p)
        print((p ^ q ^ 4) % 8)
        A //= 8
    while A > 0

this demonstrates that we actually don't care about the values of the B and C
registers across iterations. they're both overwritten before they're used.

since A is floor-divided by 8 each iteration, we know the value of A at the
start of each iteration is 8 times its value at the end of that iteration, plus
some value 0 through 7. we can check each of those possible values to see if
they print the correct value, and if so check those values against the prior
iteration, working backwards until we reach the start of the program. since the
program ends when A is 0, we can start there.
"""
