import lz77, compressors, decompressors, metrics, haffman



f = open('./data/bw_tmp.raw', 'rb')
data = f.read()
f.close()

#data = b'bananabanana'
#print('data = ', data)
print('====================')
c_data = haffman.compress(data)
print('сжато')
#print('c_data = ', c_data)
d_data = haffman.decompress(c_data)
print('====================')
#print('decompress_data = ', d_data)
print('====================')
print(data == d_data)
print(metrics.compressFactor(c_data, data))


def compress(data): # time complexity: T(n) = 2n + 1 + O(nlogn) + O(n) + 2n + 2 = 2n + O(nlogn) + O(n) + 3 = O(nlogn)
                    # space complexity: S(n) = n * n + 4 + n = O(n^2)
    matrix = [data[i:] + data[0:i] for i in range(len(data))]
    matrix.sort()
    index = matrix.index(data)
    last_col = bytes(list(map(lambda x: x[-1], matrix)))
    return index.to_bytes(2, 'big') + last_col

#print(compress(data) == c_data)


