import pandas as pd
import compressors, decompressors, metrics
def fillTable():

    f_input = open("enwik9", "r", encoding = 'utf-8')
    f_output = open("output.txt", "w", encoding="utf-8")

    enwik = f_input.read(int(1e7))
    ru_text = ''
    exe_file = ''
    bw_pic = ''
    grey_pic = ''
    color_pic = ''

    table = pd.DataFrame(columns=['Compressor', 'Data_File', 'Size_before_compression', 'Size_after_compression', 'Size_after_decompression', 'Compress_factor'])
    compressors = [compressors.HA, compressors.RLE, compressors.BWT_RLE, compressors.BWT_MTF_HA, compressors.BWT_MTF_RLE_HA, compressors.LZ77, compressors.LZ77_HA, compressors.LZ78, compressors.LZ78_HA]
    decompressors = [decompressors.HA, decompressors.RLE, decompressors.BWT_RLE, decompressors.BWT_MTF_HA, decompressors.BWT_MTF_RLE_HA, decompressors.LZ77, decompressors.LZ77_HA, decompressors.LZ78, decompressors.LZ78_HA]
    compressors_name = ['HA', 'RLE', 'BWT + RLE', 'BWT + MTF + HA', 'BWT + MTF + RLE + HA', 'LZ77', 'LZ77 + HA', 'LZ78', 'LZ78 + HA']
    
    data_files = [enwik, ru_text, exe_file, bw_pic, grey_pic, color_pic]
    data_files_name = ['enwik7', 'russian text', 'exe file', 'bw pic', 'grey pic', 'color pic']
    for i in range(len(compressors)):
        for j in range(len(data_files)):
            compress_file = compressors[i](data_files[j])
            decompress_file = decompressors[i](compress_file)
            table.loc[len(table)] = [compressors_name[i], data_files_name[i], len(data_files[j]), len(compress_file), len(decompress_file), metrics.compressFactor(len(compress_file), len(data_files[j]))]

    table.to_excel('table.xlsx', index=False)


    f_input.close()
    f_output.close()