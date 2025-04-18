SIZE = 2
BUFFER_SIZE = 1024 * 4



def find_seq(buffer, data, pos): # T(n) = O(bn) 
                                    # S(n) = 3 = O(1)
    if not buffer:
        return 0, 0
    length = 0
    max_len = 0
    offset = 0
    for i in range(len(buffer), 0, -1):
        while (pos + length) < len(data) and (i + length) < len(buffer) and data[pos:pos + length + 1] == buffer[i: i + length + 1]:
            length += 1
            if length > max_len:
                max_len = length
                offset = len(buffer) - i
    return offset, max_len
            

def compress(data, buffer_size=BUFFER_SIZE):
                                    # Time compltxity: T(n) = 3 + O(n) * (O(bn) + 2 + 3 + 3 + 2 + 1) = O(bn^2)
                                    # Space complexity: S(n) =  (O(n)) + 4 + (O(b)) + O(1) + 4 = O(n)
    compress_data = bytearray()
    pos = 0
    buffer = bytearray()
    
    while pos < len(data):
        offset, length = find_seq(buffer, data, pos) # O(bn)
        #print(offset, length)
        next_byte = data[pos + length] if pos + length < len(data) else None
        compress_data.extend(int.to_bytes(offset, SIZE, 'big') + int.to_bytes(length, SIZE, 'big') + (bytes([next_byte]) if next_byte != None else b''))
        #print(compress_data)
        buffer.extend(data[pos:pos + length + (1 if next_byte != None else 0)])
        if len(buffer) > buffer_size:
            buffer = buffer[-buffer_size:]
        pos += length + 1
        #print(buffer) 
        
    
    return bytes(compress_data)





def decompress(data, buffer_size=BUFFER_SIZE):
                                                # Time complexity: T(n) = 3 + 13n = O(n)
                                                # Space complexity: S(n) = 1 + O(n) + O(b) = O(n)
    decompress_data = bytearray()
    buffer = bytearray()
    i = 0
    while i < len(data):
        offset = int.from_bytes(data[i:i+SIZE], 'big')
        i += SIZE
        length = int.from_bytes(data[i:i+SIZE], 'big')
        i += SIZE
        next_byte = data[i] if i < len(data) else None
        i += 1
        next_seq = buffer[-offset:][:length] + (bytes([next_byte]) if next_byte != None else b'')
        decompress_data.extend(next_seq)
        buffer.extend(next_seq)
        if len(buffer) > buffer_size:
            buffer = buffer[-buffer_size:]
        #print(buffer)
        #print(i)
    #print(buffer)
    #print(decompress_data)
    return decompress_data
    



