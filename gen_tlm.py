#!/usr/bin/env python

# A script to generate windows hashes to test PTH, or for password recovery practice.
# Loosely based on David Kennedy's script
# https://www.trustedsec.com/blog/generate-an-ntlm-hash-in-3-lines-of-python/

import hashlib
import binascii
import sys

pass_2_hash = sys.argv[1]

def gen_hash(word):
    hex_hash = hashlib.new('md4', word.encode('utf-16le')).digest()
    new_hash = binascii.hexlify(hex_hash)
    return new_hash

byte_out = gen_hash(pass_2_hash)
string_out = str(byte_out)
cut_hash = string_out[2:-1]
print("NTLM hash for: " + pass_2_hash + "\n" + cut_hash)
exit()
