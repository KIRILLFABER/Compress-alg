import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import metrics, lz77

df = pd.DataFrame(columns=['buffer_size', 'compress_factor', 'correct_decompress'])


f_input = open('enwik9', 'rb')
data = f_input.read(int(1e4))
k = 3
for size in range(2 ** 3, 2 ** 12 + 1, 8 * k):
    compress_data = lz77.compress(data, window_size=size)
    decompress_data = lz77.decompress(compress_data)
    df.loc[len(df)] = [size, metrics.compressFactor(compress_data, data), decompress_data == data]
print(df)
print('===============')


fig, ax = plt.subplots()



x = df['buffer_size'].values
y = df['compress_factor'].values
ax.plot(x, y)
fig.show()
fig.savefig('./fig1.png') 




f_input.close()
