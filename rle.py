def compress(data):
    data += b"#"
    c = 1
    notRepeatCounter = 0
    comp_data = b""
    prev_byte = data[0]
    l = b""

    for byte in data[1:]:
        if byte == prev_byte:
            c += 1
            if notRepeatCounter != 0:
                comp_data += bytes([notRepeatCounter + 128]) + l
                l = b""
                notRepeatCounter = 0
        else:
            if c == 1:
                l += bytes([prev_byte])
                notRepeatCounter += 1
            else:
                comp_data += bytes([c]) + bytes([prev_byte])
            prev_byte = byte
            c = 1

    if notRepeatCounter != 0:
        comp_data += bytes([notRepeatCounter + 128]) + l

    return comp_data


def decompress(data):
    decomp_data = b""
    i = 0

    while i < len(data):
        byte = data[i]
        if byte >= 128:
            count = byte - 128
            decomp_data += data[i + 1:i + 1 + count]
            i += 1 + count
        else:
            count = byte
            decomp_data += bytes([data[i + 1]]) * count
            i += 2

    return decomp_data
