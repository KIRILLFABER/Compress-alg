import pandas as pd
import compressors, decompressors, metrics
def fillTable():

    f_input = open("enwik9", "rb")
    f_output = open("output.txt", "w", encoding="utf-8")

    enwik = f_input.read(int(1e4))
    ru_text = ''
    exe_file = ''
    bw_pic = ''
    grey_pic = ''
    color_pic = ''

    table = pd.DataFrame(columns=['Compressor', 'Data_File', 'Size_before_compression', 'Size_after_compression', 'Size_after_decompression', 'Compress_factor'])
    compressors_arr = [compressors.HA, compressors.RLE, compressors.BWT_RLE, compressors.BWT_MTF_HA, compressors.BWT_MTF_RLE_HA]
    decompressors_arr = [decompressors.HA, decompressors.RLE, decompressors.BWT_RLE, decompressors.BWT_MTF_HA, decompressors.BWT_MTF_RLE_HA]
    compressors_name = ['HA', 'RLE', 'BWT + RLE', 'BWT + MTF + HA', 'BWT + MTF + RLE + HA']
    
    data_files = [enwik]
    data_files_name = ['enwik7']
    for i in range(len(compressors_arr)):
        for j in range(len(data_files)):
            compress_file = compressors_arr[i](data_files[j])
            decompress_file = decompressors_arr[i](compress_file)
            table.loc[len(table)] = [compressors_name[i], data_files_name[j], len(data_files[j]), len(compress_file), len(decompress_file), metrics.compressFactor(len(compress_file), len(data_files[j]))]

    table.to_excel('table.xlsx', index=False)


    f_input.close()
    f_output.close()