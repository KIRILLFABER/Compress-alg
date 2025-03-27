import haffman, bwt, lz77, lz78, mtf, rle, metrics

# 1. HA
def HA(data):
    return haffman.compress(data)


# 2. Run-length encoding (RLE)

def RLE(data):
    return rle.compress(data)



# 3. BWT + RLE
def BWT_RLE(data, block_size = 1024 * 4):
    bwt_result = b''
    for block in [data[i:i + block_size] for i in range(0, len(data), block_size)]:
        bwt_result += bwt.compress(block)
    return rle.compress(bwt_result)

# 4. BWT + MTF + HA
def BWT_MTF_HA(data, block_size = 1024 * 4):
    bwt_result = b''
    for block in [data[i:i + block_size] for i in range(0, len(data), block_size)]:
        bwt_result += bwt.compress(block)

    mtf_result = mtf.compress(bwt_result)
    ha_result = haffman.compress(mtf_result)
    return ha_result



# 5. BWT + MTF + RLE + HA
def BWT_MTF_RLE_HA(data, block_size = 1024 * 4):
    bwt_result = b''
    for block in [data[i:i + block_size] for i in range(0, len(data), block_size)]:
        bwt_result += bwt.compress(block)
    mtf_result = mtf.compress(bwt_result)
    rle_result = rle.compress(mtf_result)
    ha_result = haffman.compress(rle_result)
    return ha_result

# 6. LZ77

def LZ77(data):
    return lz77.compress(data)

# 7. LZ77 + HA
def LZ77_HA(data):
    lz77_result = lz77.compress(data)
    return haffman.compress(lz77_result)

# 8. LZ78
def LZ78(data):
    return lz78.compress(data)

# 9. LZ78 + HA
def LZ78_HA(data):
    lz78_result = lz78.compress(data)
    return haffman.compress(lz78_result)

    