

def compress(data, window_size=20, lookahead_buffer_size=10):
    compressed_data = []
    i = 0
    while i < len(data):
        search_buffer_start = max(0, i - window_size)
        search_buffer = data[search_buffer_start:i]
        lookahead_buffer = data[i:i + lookahead_buffer_size]

        offset, length, next_char = find_longest_match(search_buffer, lookahead_buffer)

        compressed_data.append((offset, length, next_char))
        i += length + 1

    return compressed_data

def decompress(compressed_data):
    decompressed_data = []
    for item in compressed_data:
        offset, length, next_char = item
        if length > 0:
            start = len(decompressed_data) - offset
            for i in range(length):
                decompressed_data.append(decompressed_data[start + i])
        decompressed_data.append(next_char)
    return bytes(decompressed_data) if isinstance(decompressed_data[0], int) else ''.join(decompressed_data)

def find_longest_match(search_buffer, lookahead_buffer):
    length = 0
    offset = 0
    next_char = lookahead_buffer[0] if lookahead_buffer else ''

    for i in range(1, len(lookahead_buffer) + 1):
        substring = lookahead_buffer[:i]
        match_index = search_buffer.rfind(substring)
        if match_index != -1:
            offset = len(search_buffer) - match_index
            length = len(substring)
            next_char = lookahead_buffer[i] if i < len(lookahead_buffer) else ''
        else:
            break

    return offset, length, next_char