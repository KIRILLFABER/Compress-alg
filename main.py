import haffman, bwt, lz77, lz78, mtf, rle, metrics, compressors, decompressors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fillTable
# import tmp ###





if __name__ == "__main__":
    match(int(input("Заполнить таблицу? 1 - Да, остальное - нет: "))):
        case 1:
            fillTable.fillTable()
        case _:
            pass

    


   