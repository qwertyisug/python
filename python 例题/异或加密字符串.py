import os
import sys
import struct
 
def enc(path, key):
    path_ret = ""
    for i in range(0, len(path)/4):
        path_ret += struct.pack("<L", struct.unpack("<L", path[i*4 : (i*4)+4])[0] ^ key)
 
    return path_ret
 
print enc("daniel King ", 0x0)
print enc("daniel King ", 0xFFFFFFFF)
print enc(enc("daniel King ", 0xFFFFFFFF), 0xFFFFFFFF)
