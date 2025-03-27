import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import metrics, lz77

df = pd.DataFrame(columns=['buffer_size', 'data_file', 'compress_factor', 'correct_decompress'])

data_path = './data/'
data_files = []
data_files_name = ['enwik7', 'ru_text.txt', 'exe_file.exe', 'img.CR2', 'grey_img.raw', 'bw_img.raw']
for name in data_files_name:
        f_input = open(data_path + name, 'rb')
        file = f_input.read()
        f_input.close()
        data_files.append(file)
        print('file - ', name)
k = 3
for size in range(2 ** 5, 2 ** 8, 8 * k):
    for i in range(len(data_files)):
        compress_data = lz77.compress(data_files[i], lookahead_size=size)
        decompress_data = lz77.decompress(compress_data)
        df.loc[len(df)] = [size, data_files_name[i], metrics.compressFactor(compress_data, data_files[i]), decompress_data == data_files[i]]
        print(size)
print(df)
print('===============')

fig, ax = plt.subplots(len(data_files), 1, figsize = (100, 100))
for i in range(len(data_files)):
     x = df[df['data_file'] == data_files_name[i]]['buffer_size'].values
     y = df[df['data_file'] == data_files_name[i]]['compress_factor'].values
     ax[i].plot(x, y, label=data_files_name[i])
     ax[i].set_xlabel("buff_size")
fig.show()
fig.savefig('./buffer_size_lz77.png') 




f_input.close()
