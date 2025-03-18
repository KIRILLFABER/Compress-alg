

def compress(text): # time complexity:s
    matrix = [text[i:] + text[0:i] for i in range(len(text))]
    matrix.sort()
    index = matrix.index(text)
    last_col = "".join(list(map(lambda x: x[-1], matrix)))
    [print(i) for i in matrix]
    print(index)


    return (index, last_col)



# Доделать
def decompress(index, last_col):
    matrix = ["" for i in range(len(last_col))]
    for _ in range(len(last_col)):
        for j in range(len(last_col)):
            matrix[j] = last_col[j] + matrix[j]
        matrix.sort()
    return matrix[index]
    



    # banana

        



