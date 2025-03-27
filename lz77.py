import struct
from collections import defaultdict

def compress(data, window_size=8192, lookahead_size=90):
    
    compressed = bytearray()
    pos = 0
    length = len(data)
    
    hash_table = defaultdict(list)
    
    while pos < length:
        best_offset = 0
        best_len = 0
        remaining = length - pos
        current_lookahead = min(lookahead_size, remaining)
        
        if current_lookahead > 0:
            max_offset = min(window_size, pos)
            

            if remaining >= 3:
                key = data[pos:pos+3]
                for candidate in hash_table.get(key, []):
                    if pos - candidate > max_offset:
                        continue
                    
                    match_len = 0
                    while (match_len < current_lookahead and
                           data[candidate + match_len] == data[pos + match_len]):
                        match_len += 1
                    
                    if match_len > best_len:
                        best_offset = pos - candidate
                        best_len = match_len
                        if best_len == current_lookahead:
                            break
            
            if remaining >= 3:
                hash_table[data[pos:pos+3]].append(pos)

                if len(hash_table[key]) > 32:
                    hash_table[key] = hash_table[key][-16:]
        next_char_pos = pos + best_len
        next_char = data[next_char_pos] if next_char_pos < length else 0
        compressed.extend(struct.pack('>HB', best_offset, best_len))
        if best_len < remaining:
            compressed.append(next_char)
        
        pos += best_len + 1 if best_len < remaining else best_len
    
    return bytes(compressed)

def decompress(compressed):
    decompressed = bytearray()
    pos = 0
    length = len(compressed)
    
    while pos + 2 < length:
        offset = compressed[pos] << 8 | compressed[pos+1]
        ln = compressed[pos+2]
        pos += 3
        
        if offset > 0:
            start = len(decompressed) - offset
            if start >= 0 and ln > 0:
                end = start + ln
                if end <= len(decompressed):
                    decompressed.extend(decompressed[start:end])
                else:
                    repeat = ln // offset
                    remainder = ln % offset
                    for _ in range(repeat):
                        decompressed.extend(decompressed[start:start+offset])
                    if remainder:
                        decompressed.extend(decompressed[start:start+remainder])
        
        if pos < length:
            decompressed.append(compressed[pos])
            pos += 1
    
    return bytes(decompressed)