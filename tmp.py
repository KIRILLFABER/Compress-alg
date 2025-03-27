import compressors, decompressors, bwt
import time








f_input = open('enwik7', 'rb')
f_comp = open('COMP', 'wb')
f_decomp = open('DECOMP.exe', 'wb')
data = f_input.read()
comp_data = compressors.BWT_RLE(data)
decomp_data = decompressors.BWT_RLE(comp_data)
print(data == decomp_data)
#print('comp data ', comp_data)
#print('decomp data', decomp_data)




#f_comp.write(comp_data)
#f_decomp.write(decomp_data)





f_input.close()
f_comp.close()
f_decomp.close()