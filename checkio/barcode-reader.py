#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

L = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
R = ["".join("01"[digit == "0"] for digit in item) for item in L]
G = [item[::-1] for item in R]
Groups = ["LLLLLL","LLGLGG","LLGGLG","LLGGGL","LGLLGG","LGGLLG","LGGGLL","LGLGLG","LGLGGL","LGGLGL"]

def barcode_reader(barcode):
    c1, c2, c3 = barcode[:3], barcode[45:50], barcode[-3:]
    if not (c1 == c3 == "_ _" and c2 == " _ _ "): return None

    def decode(raw) -> str:

        def chunk(start, end):
            for i in range(start, end, 7): yield raw[i:i + 7]
        
        code, left_structure = "", ""
        for left in chunk(3, 45):
            if left in L:
                code += str(L.index(left))
                left_structure += "L"
            elif left in G:
                code += str(G.index(left))
                left_structure += "G"
            else: return None

        if not all(rights := [str(R.index(right)) if right in R else None for right in chunk(50, 92)]): return None
        code = str(Groups.index(left_structure)) + code + "".join(rights)
        
        # checksum
        return [code, None][sum([[1,3][i%2] * int(c) for i, c in enumerate(str(code))]) % 10]
    
    raw = "".join([str(int(_ == "_")) for _ in barcode])
    return decode(raw) or decode(raw[::-1])

if __name__ == '__main__':
    assert barcode_reader(
        '_ _   _ __ _  ___ __  __  _  __ ____ _  ___ _ _ _ __  __ __ __  _    _ _ ___  _  ___ _   _  _ _'
    ) == '5901234123457', '5901234123457'

    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) == '4299687613665', '4299687613665'

    assert barcode_reader(
        '_ _ ___ __  __  _  _  __ ____ _ _   __ __   _ _ _ _ _    _   _  _  _   ___ _  __  __ __ __  _ _'
    ) is None, '0712345678912 : wrong check digit (right: 1)'

    assert barcode_reader(
        '___  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) is None, 'wrong left guard bar'
    
    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ ___ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) is None, 'wrong center bar'

    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ ___'
    ) == None, 'wrong right guard bar'

    print("Check done.")

