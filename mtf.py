
def compress(text, l = []):
    l = [chr(i) for i in range(128)]
    #[print(f'{i} - {l[i]}') for i in range(len(l))]
    result = []
    for i in text:
        result.append(l.index(i))
        l.pop(l.index(i))
        l.insert(0, i)
    print(result)
    return result
        








def decompress(seq, l):
    decomp_text = ''
    for i in seq:
        d = l.pop(i)
        decomp_text += d
        l.insert(0, d)
    print(decomp_text)


decompress(compress("bananaaa"), l = [chr(i) for i in range(128)])