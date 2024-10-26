#!/usr/bin/env python3

from random import randint
from Crypto.Util.number import bytes_to_long, long_to_bytes

ctxt = long_to_bytes(0x57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637);
key = b'Africa!';

def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt


random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

ctxt = encrypt(ctxt, random_strs[2]);
ctxt = encrypt(ctxt, random_strs[3]);
ctxt = encrypt(ctxt, random_strs[4]);

flag = encrypt(ctxt, key);
print(flag);