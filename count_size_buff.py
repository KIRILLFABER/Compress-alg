import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import metrics, lz77
import time

df = pd.DataFrame(columns=['buffer_size', 'data_file', 'time', 'compress_factor', 'correct_decompress'])

data_path = './data/'
data_files = []
#data_files_name = ['enwik7', 'ru_text.txt', 'exe_file.exe', 'img.CR2', 'grey_img.raw', 'bw_img.raw']
data_files_name = ['enwik7']
for name in data_files_name:
        f_input = open(data_path + name, 'rb')
        file = f_input.read()
        f_input.close()
        data_files.append(file)
        print('file - ', name)
for size in range(1024, 1024 * 5, 1024):
    for i in range(len(data_files)):
        start = time.time()
        compress_data = lz77.compress(data_files[i], buffer_size=size)
        decompress_data = lz77.decompress(compress_data, buffer_size=size)
        end = time.time()
        t = (end - start) / 60
        df.loc[len(df)] = [size, data_files_name[i], t, metrics.compressFactor(compress_data, data_files[i]), decompress_data == data_files[i]]
        print(size)
print(df)
print('===============')

fig, ax = plt.subplots(1, 2, figsize = (100, 100))

x = df['buffer_size'].values
y = df['compress_factor'].values
ax[0].plot(x, y, label=data_files_name[0])
ax[0].set_xlabel("buff_size")
ax[0].set_ylabel('compress_factor')
y = df['time'].values
ax[1].plot(x, y, label = data_files_name[0])
ax[1].set_xlabel('buff_size')
ax[1].set_ylabel('time')
fig.show()
fig.savefig('./buffer_size_lz77.png') 




