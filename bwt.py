

def compress(data): # time complexity:
    matrix = [data[i:] + data[0:i] for i in range(len(data))]
    matrix.sort()
    index = matrix.index(data)
    last_col = bytes(list(map(lambda x: x[-1], matrix)))
    return index.to_bytes(4, 'big') + last_col



# Доделать
def decompress(data):
    index = int.from_bytes(data[:4], 'big')
    data = data[4:]
    matrix = [b"" for i in range(len(data))]
    for _ in range(len(data)):
        for j in range(len(data)):
            matrix[j] = bytes([data[j]]) + matrix[j]
        matrix.sort()
    return matrix[index]
    



    # banana

        



