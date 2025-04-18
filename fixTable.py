import pandas as pd
import compressors, decompressors, metrics


df = pd.read_excel('table.xlsx')


compressors_list = [compressors.HA, compressors.RLE, compressors.BWT_RLE, compressors.BWT_MTF_HA, compressors.BWT_MTF_RLE_HA, compressors.LZ77, compressors.LZ77_HA, compressors.LZ78, compressors.LZ78_HA]
decompressors_list = [decompressors.HA, decompressors.RLE, decompressors.BWT_RLE, decompressors.BWT_MTF_HA, decompressors.BWT_MTF_RLE_HA, decompressors.LZ77, decompressors.LZ77_HA, decompressors.LZ78, decompressors.LZ78_HA]
compressors_name = ['HA', 'RLE', 'BWT + RLE', 'BWT + MTF + HA', 'BWT + MTF + RLE + HA', 'LZ77', 'LZ77 + HA', 'LZ78', 'LZ78 + HA']
data_files = []
data_files_name = ['enwik7', 'ru_text.txt', 'exe_file.exe', 'img.raw', 'grey_img.raw', 'bw_img.raw']
data_path = './data/'
comp_path = './compress_data/'
decomp_path = './decompress_data/'
for name in data_files_name:
    f_input = open(data_path + name, 'rb')
    file = f_input.read()
    f_input.close()
    data_files.append(file)
    print('file - ', name)

com = 1

for i in range(len(compressors_list)):
            if (com == 9):
                  break
            for j in range(len(data_files)):
                print('compressor - ', compressors_name[i])
                print('file - ', data_files_name[j])
                com = int(input(f'fix? - '))
                if (com == 1):
                    compress_file = compressors_list[i](data_files[j])
                    decompress_file = decompressors_list[i](compress_file)
                    df.loc[(df["Compressor"] == compressors_name[i]) & (df["Data_File"] == data_files_name[j])]= [compressors_name[i], data_files_name[j], len(data_files[j]), len(compress_file), len(decompress_file), metrics.compressFactor(compress_file, data_files[j]), data_files[j] == decompress_file]
                    f_comp = open(comp_path + compressors_name[i] + '_comp_' + data_files_name[j], 'wb')
                    f_decomp = open(decomp_path + compressors_name[i] + '_decomp_' + data_files_name[j], 'wb')
                    f_comp.write(compress_file)
                    f_decomp.write(decompress_file)
                    
                


                    f_comp.close()
                    f_decomp.close()
                elif (com == 9):
                      break


print(df)

df.to_excel("table.xlsx", index = False)

