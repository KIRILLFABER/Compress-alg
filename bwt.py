

def compress(data): # time complexity: T(n) = 2n + 1 + O(nlogn) + O(n) + 2n + 2 = 2n + O(nlogn) + O(n) + 3 = O(nlogn)
                    # space complexity: S(n) = n * n + 4 + n = O(n^2)
    matrix = [data[i:] + data[0:i] for i in range(len(data))]
    matrix.sort()
    index = matrix.index(data)
    last_col = bytes(list(map(lambda x: x[-1], matrix)))
    return index.to_bytes(2, 'big') + last_col



def decompress(last_column_BWM): # time compltxity: T(n) = 1 + 3 + 1 + 1 + O(n) + 2 + 3n = O(n)
                                # space complexity: S(n) = 2 + n - 2 + 4 + n + 4 + 4 + n = O(n)
    if not last_column_BWM:
        return b""
    

    S_index = int.from_bytes(last_column_BWM[:2], 'big')
    last_column_BWM = last_column_BWM[2:]
    N = len(last_column_BWM)
    P_inverse = counting_sort_arg_bytes(last_column_BWM)
    reconstructed = bytearray()
    j = S_index
    for _ in range(N):
        if j >= len(P_inverse): 
            break
        j = P_inverse[j]
        reconstructed.append(last_column_BWM[j])
    
    return bytes(reconstructed)

def counting_sort_arg_bytes(S):
    N = len(S)
    if N == 0:
        return []
    
    M = 256 
    
    counts = [0] * M
    for b in S:
        counts[b] += 1
    
    pos = [0] * M
    for i in range(1, M):
        pos[i] = pos[i-1] + counts[i-1]
    
    P_inverse = [0] * N
    temp_pos = pos.copy()
    for i, b in enumerate(S):
        P_inverse[temp_pos[b]] = i
        temp_pos[b] += 1
    
    return P_inverse



    # banana
    # aaabnn

        
# def counting_sort(data):
#     if not data:
#         return b""

#     counts = [0] * 256
#     for byte in data:
#         counts[byte] += 1
    
#     sorted_data = bytearray()
#     for byte in range(256):
#         sorted_data.extend([byte] * counts[byte])
    
#     return bytes(sorted_data)

