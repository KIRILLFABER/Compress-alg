import haffman, bwt, lz77, lz78, mtf, rle, metrics, compressors, decompressors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fillTable
import tmp ###





if __name__ == "__main__":
    tmp.fillTable()
    f_input = open('enwiki.txt', 'rb')
    data = f_input.read(int(1000))
    print(len(data) > len(compressors.HA(data)))
    print(data == decompressors.HA(compressors.HA(data)))
    
    


    # entorpy of BWT + MTF
    # block_sizes = [i for i in range(1000, 10000, 1000)]
    # ent = []
    # for block_size in range(50000, 100000, 10000):
    #     print(f'block_size = {block_size}')
    #     blocks = [text[i: i + block_size] for i in range(0, len(text) // 10, block_size)]
    #     compressed_blocks = []
    #     i = 1
    #     for block in blocks:
    #         bwt_index, bwt_result = bwt.compress(block)
    #         mtf_result = mtf.compress(bwt_result)
    #         compressed_blocks.append(mtf_result)
    #         print(i, '\t', len(blocks))
    #         i+= 1
    #     compressed_text = ''
    #     for block in compressed_blocks:
    #         compressed_text += ''.join([str(i) for i in block])
    #     ent.append(metrics.entropy(metrics.prob(compressed_text)))

    # Verify
    print('HA - ', data == decompressors.HA(compressors.HA(data)))
    print('RLE - ', data == decompressors.RLE(compressors.RLE(data)))
    print('BWT + RLE - ', data == decompressors.BWT_RLE(compressors.BWT_RLE(data)))
    print('BWT + MTF + HA - ', data == decompressors.BWT_MTF_HA(compressors.BWT_MTF_HA(data)))
    print('BWT + MTF + RLE + HA - ', data == decompressors.BWT_MTF_RLE_HA(compressors.BWT_MTF_RLE_HA(data)))

    
    
    
    
    # fig, ax = plt.subplots()
    # ax.plot(block_sizes, ent)

    # fig.savefig('./fig1.png')   
    


    f_input.close()


# print(metrics.compressFactor(result))
# print(metrics.entropy(metrics.prob(result)))


# print(metrics.entropy([0.25,0.25,0.25,0.25]))