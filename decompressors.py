import haffman, bwt, lz77, lz78, mtf, rle, metrics

# 1. HA
def HA(data):
    return haffman.decompress(data)


# 2. Run-length encoding (RLE)

def RLE(data):
    return rle.decompress(data)



# 3. BWT + RLE
def BWT_RLE(data):
    rle_decomp = rle.decompress(data)
    return bwt.decompress(rle_decomp)

# 4. BWT + MTF + HA
def BWT_MTF_HA(data):
    ha_decomp = haffman.decompress(data)
    mtf_decomp = mtf.decompress(ha_decomp)
    bwt_decomp = bwt.decompress(mtf_decomp)
    return bwt_decomp




# 5. BWT + MTF + RLE + HA
def BWT_MTF_RLE_HA(data):
    ha_decomp = haffman.decompress(data)
    rle_decomp = rle.decompress(ha_decomp)
    mtf_decomp = mtf.decompress(rle_decomp)
    bwt_decomp = bwt.decompress(mtf_decomp)
    return bwt_decomp
    

# 6. LZ77

def LZ77(text):
    return ''

# 7. LZ77 + HA
def LZ77_HA(text):
    return ''

# 8. LZ78
def LZ78(text):
    return ''

# 9. LZ78 + HA
def LZ78_HA(text):
    return ''

    
