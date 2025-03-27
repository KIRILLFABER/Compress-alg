import haffman, bwt, lz77, lz78, mtf, rle, metrics

# 1. HA
def HA(data):
    return haffman.decompress(data)


# 2. Run-length encoding (RLE)

def RLE(data):
    return rle.decompress(data)



# 3. BWT + RLE
def BWT_RLE(data, block_size = 1024 * 4 + 2):
    data = rle.decompress(data)
    bwt_result = b''
    for block in [data[i:i + block_size] for i in range(0, len(data), block_size)]:
        bwt_result += bwt.decompress(block)
    return bwt_result

# 4. BWT + MTF + HA
def BWT_MTF_HA(data, block_size = 1024 * 4 + 2):
    ha_decomp = haffman.decompress(data)
    mtf_decomp = mtf.decompress(ha_decomp)
    data = mtf_decomp
    bwt_decomp = b''
    for block in [data[i:i + block_size] for i in range(0, len(data), block_size)]:
        bwt_decomp += bwt.decompress(block)
    return bwt_decomp




# 5. BWT + MTF + RLE + HA
def BWT_MTF_RLE_HA(data, block_size = 1024 * 4 + 2):
    ha_decomp = haffman.decompress(data)
    rle_decomp = rle.decompress(ha_decomp)
    mtf_decomp = mtf.decompress(rle_decomp)
    data = mtf_decomp
    bwt_decomp = b''
    for block in [data[i:i + block_size] for i in range(0, len(data), block_size)]:
        bwt_decomp += bwt.decompress(block)
    return bwt_decomp
    

# 6. LZ77

def LZ77(data):
    return lz77.decompress(data)

# 7. LZ77 + HA
def LZ77_HA(data):
    ha_decomp = haffman.decompress(data)
    return lz77.decompress(ha_decomp)

# 8. LZ78
def LZ78(data):
    return lz78.decompress(data)

# 9. LZ78 + HA
def LZ78_HA(data):
    ha_decomp = haffman.decompress(data)
    return lz78.decompress(ha_decomp)

    