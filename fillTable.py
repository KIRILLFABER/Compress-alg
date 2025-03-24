import pandas as pd
import numpy as np
import compressors, decompressors, metrics
def fillTable():
    table = pd.DataFrame(columns=['Compressor', 'Data_File', 'Size_before_compression', 'Size_after_compression', 'Size_after_decompression', 'Compress_factor', 'Correct_decompress'])
    compressors_list = [compressors.HA, compressors.RLE, compressors.BWT_RLE, compressors.BWT_MTF_HA, compressors.BWT_MTF_RLE_HA, compressors.LZ77, compressors.LZ77_HA, compressors.LZ78, compressors.LZ78_HA]
    decompressors_list = [decompressors.HA, decompressors.RLE, decompressors.BWT_RLE, decompressors.BWT_MTF_HA, decompressors.BWT_MTF_RLE_HA, decompressors.LZ77, decompressors.LZ77_HA, decompressors.LZ78, decompressors.LZ78_HA]
    compressors_name = ['HA', 'RLE', 'BWT + RLE', 'BWT + MTF + HA', 'BWT + MTF + RLE + HA', 'LZ77', 'LZ77 + HA', 'LZ78', 'LZ78 + HA']
    data_files = []
    data_files_name = ['enwik9', 'ru_text.txt', 'exe_file.exe', 'img.bmp', 'img.bmp', 'img.bmp']
    size = int(1e3)
    comp_path = './compress_data/'
    decomp_path = './decompress_data/'
    for name in data_files_name:
        f_input = open(name, 'rb')
        file = f_input.read(size)
        f_input.close()
        data_files.append(file)
        print('file - ', name)
    for i in range(len(compressors_list)):
        for j in range(len(data_files)):
            print('compressor - ', compressors_name[i])
            print('file - ', data_files_name[j])
            compress_file = compressors_list[i](data_files[j])
            decompress_file = decompressors_list[i](compress_file)
            table.loc[len(table)] = [compressors_name[i], data_files_name[j], len(data_files[j]), len(compress_file), len(decompress_file), metrics.compressFactor(compress_file, data_files[j]), data_files[j] == decompress_file]
            f_comp = open(comp_path + compressors_name[i] + '_comp_' + data_files_name[j], 'wb')
            f_decomp = open(decomp_path + compressors_name[i] + '_decomp_' + data_files_name[j], 'wb')
            f_comp.write(compress_file)
            f_decomp.write(decompress_file)


            f_comp.close()
            f_decomp.close()

    table.to_excel('table.xlsx', index=False)

