
def compress(data, l = []):
    l = [bytes([i]) for i in range(256)]
    #[print(f'{i} - {l[i]}') for i in range(len(l))]
    result = b''
    for i in data:
        result += bytes([l.index(bytes([i]))])
        l.pop(l.index(bytes([i])))
        l.insert(0, bytes([i]))
    #print(result)
    return result
        








def decompress(data, l = []):
    l = [bytes([i]) for i in range(256)]
    decomp_data = b''
    for i in data:
        d = l.pop(i)
        decomp_data += d
        l.insert(0, d)
    return decomp_data


