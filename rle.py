def compress(text): # T(n) = 6 + (n - 1)(1 + 1 + 2) + 4 = 6 + 4n - 4 + 4 = 4n + 6 = O(n)
    text += "#"
    c = 1
    notRepeatCounter = 0
    comp_text = ""
    prev_s = text[0]
    l = ""

    for s in text[1:]:
        if s == prev_s:
            c += 1
            comp_text += (chr(notRepeatCounter + 128) if notRepeatCounter != 0 else '')  + l
            l = ''
            notRepeatCounter = 0
        else:
            if (c == 1):
                l += prev_s
                prev_s = s
                notRepeatCounter += 1
            else:
                comp_text += chr(c) + prev_s
                prev_s = s
                c = 1
    comp_text += (chr(notRepeatCounter + 128) if notRepeatCounter != 0 else '')  + l
            
                

    return comp_text
            

def decompress(text):
    decomp_text = ''
    notRepeatFlag = False
    i = 0
    while i < len(text):
        if ord(text[i]) >= 128:
            c = ord(text[i]) - 128 # кол-во неповторяющихся символов
            decomp_text += text[i + 1:i + c + 1]
            i += c + 1
        else:
            decomp_text += text[i + 1] * ord(text[i])
            i += 2
    return decomp_text



        
            




# aaaaabcdefff
# 5a(133)bcde3f



