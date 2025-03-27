import struct
from collections import defaultdict

def compress(data, max_dict_size=65535):
    dictionary = {b'': 0}
    next_code = 1
    compressed = bytearray()
    w = b''
    
    for byte in data:
        c = bytes([byte])
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed.extend(struct.pack('>H', dictionary[w]))
            compressed.append(byte)
            
            if next_code < max_dict_size:
                dictionary[wc] = next_code
                next_code += 1
            w = b''
    
    if w:
        last_byte = w[-1:]
        prefix = w[:-1]
        compressed.extend(struct.pack('>H', dictionary[prefix]))
        compressed.append(ord(last_byte))
    
    return bytes(compressed)

def decompress(compressed, max_dict_size=65535):
    dictionary = {0: b''}
    next_code = 1
    decompressed = bytearray()
    pos = 0
    
    while pos + 2 < len(compressed):
        code = (compressed[pos] << 8) | compressed[pos+1]
        byte = compressed[pos+2]
        pos += 3
        
        
        phrase = dictionary[code] + bytes([byte])
        decompressed.extend(phrase)
        
        if next_code < max_dict_size:
            dictionary[next_code] = phrase
            next_code += 1
    
    if pos < len(compressed):
        decompressed.extend(compressed[pos:])
    
    return bytes(decompressed)