import haffman, bwt, lz77, lz78, mtf, rle, metrics







if __name__ == "__main__":
    print(123)
    f_input = open("enwiki.txt", "r", encoding="utf-8")
    f_output = open("output.txt", "w", encoding="utf-8")

    text = f_input.read()
    


    f_input.close()
    f_output.close()


# print(metrics.compressFactor(result))
# print(metrics.entropy(metrics.prob(result)))


# print(metrics.entropy([0.25,0.25,0.25,0.25]))