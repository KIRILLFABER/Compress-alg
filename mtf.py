def compress(data): # time complexity: T(n) = 1 + 1 + 4n = O(n)
                    # space complexity: S(n) = 256 * 4 + 4 + 4n = O(n)
    alphabet = list(range(256)) 
    result = bytearray()
    
    for byte in data:
        idx = alphabet.index(byte)
        result.append(idx)
        alphabet.pop(idx)
        alphabet.insert(0, byte)
    
    return bytes(result)

def decompress(data):
                        # time complexity: T(n) = O(n)
                        # space complexity: S(n) = O(n)
    alphabet = list(range(256))
    result = bytearray()
    
    for idx in data:
        byte = alphabet[idx]
        result.append(byte)
        alphabet.pop(idx)
        alphabet.insert(0, byte)
    
    return bytes(result)