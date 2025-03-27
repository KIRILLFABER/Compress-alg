import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bwt, mtf
import metrics


f_input = open('./data/enwik7', 'rb')
data = f_input.read()


f_input.close()

x = []
y = []
for block_size in range(1024 * 1, 1024 * 10, 1024):
    bwt_result = b''
    for i in range(0, len(data), block_size):
        bwt_result += bwt.compress(data[i: i + block_size])
    mtf_result = mtf.compress(bwt_result)
    print(block_size)
    x.append(block_size)
    y.append(metrics.entropy(mtf_result))
fig, ax = plt.subplots()

ax.plot(np.array(x), np.array(y))
ax.set_xlabel('block_size')
ax.set_ylabel('entropy')
fig.savefig('./block_size_BWT_MTF.png')