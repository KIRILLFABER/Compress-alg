def compress(data, byte_count=2):
    if not data:
        return b""
    
    max_count = (1 << (8 * byte_count)) - 1 
    comp_data = bytearray()
    buffer = bytearray()
    prev_byte = data[0]
    count = 1
    
    for byte in data[1:]:
        if byte == prev_byte and count < max_count:
            count += 1
        else:
            if count > 1:
                if buffer:
                    comp_data.extend((len(buffer) | (1 << (8 * byte_count - 1))).to_bytes(byte_count, 'big'))
                    comp_data.extend(buffer)
                    buffer.clear()
                comp_data.extend(count.to_bytes(byte_count, 'big'))
                comp_data.append(prev_byte)
            else:
                buffer.append(prev_byte)
                if len(buffer) >= max_count:
                    comp_data.extend((max_count | (1 << (8 * byte_count - 1))).to_bytes(byte_count, 'big'))
                    comp_data.extend(buffer[:max_count])
                    buffer = buffer[max_count:]
            count = 1
            prev_byte = byte
    if count > 1:
        if buffer:
            comp_data.extend((len(buffer) | (1 << (8 * byte_count - 1))).to_bytes(byte_count, 'big'))
            comp_data.extend(buffer)
        comp_data.extend(count.to_bytes(byte_count, 'big'))
        comp_data.append(prev_byte)
    else:
        buffer.append(prev_byte)
        if buffer:
            comp_data.extend((len(buffer) | (1 << (8 * byte_count - 1))).to_bytes(byte_count, 'big'))
            comp_data.extend(buffer)
    
    return bytes(comp_data)

def decompress(data, byte_count=2):
    if not data:
        return b""
    
    decomp_data = bytearray()
    i = 0
    n = len(data)
    mask = 1 << (8 * byte_count - 1)
    
    while i < n:
        if i + byte_count > n:
            raise ValueError("Invalid compressed data")
        
        count = int.from_bytes(data[i:i+byte_count], 'big')
        i += byte_count
        
        if count & mask:
            true_count = count & ~mask
            if i + true_count > n:
                raise ValueError("Invalid compressed data")
            decomp_data.extend(data[i:i+true_count])
            i += true_count
        else:
            byte = data[i]
            decomp_data.extend([byte] * count)
            i += 1
    
    return bytes(decomp_data)