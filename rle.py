def compress(data, byte_count=2):
    data += b"#"
    c = 1
    notRepeatCounter = 0
    comp_data = b""
    prev_byte = data[0]
    l = b""

    max_count = (1 << (8 * byte_count - 1)) - 1  # Максимальное значение для счетчика

    for byte in data[1:]:
        if byte == prev_byte:
            c += 1
            if notRepeatCounter != 0:
                comp_data += (notRepeatCounter + (1 << (8 * byte_count - 1))).to_bytes(byte_count, 'big') + l
                l = b""
                notRepeatCounter = 0
        else:
            if c == 1:
                l += bytes([prev_byte])
                notRepeatCounter += 1
            else:
                comp_data += c.to_bytes(byte_count, 'big') + bytes([prev_byte])
                c = 1
            prev_byte = byte

    if notRepeatCounter != 0:
        comp_data += (notRepeatCounter + (1 << (8 * byte_count - 1))).to_bytes(byte_count, 'big') + l

    return comp_data

def decompress(data, byte_count=2):
    decomp_data = b""
    i = 0

    while i < len(data):
        count_bytes = data[i:i + byte_count]
        count = int.from_bytes(count_bytes, 'big')
        i += byte_count

        if count & (1 << (8 * byte_count - 1)):  # Проверка старшего бита
            count -= (1 << (8 * byte_count - 1))
            decomp_data += data[i:i + count]
            i += count
        else:
            decomp_data += bytes([data[i]]) * count
            i += 1

    return decomp_data