#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def checkio(text, word):
    lines = text.replace(" ", "").lower().splitlines()
   
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            for i_offset, j_offset in [(1, len(word)), (len(word), 1)]:
                new_i_offset, new_j_offset = i + i_offset, j + j_offset
                if new_i_offset > len(lines): continue
                if new_j_offset > len(lines[i]): continue
                if "".join([letter for line in lines[i:new_i_offset] for letter in line[j:new_j_offset]]) == word:
                    return [i + 1, j + 1, new_i_offset, new_j_offset]

    return []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe;\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.","stog") == [1,19,4,19]
    assert checkio("Hi all!\nAnd all goodbye!\nOf course goodbye.\nor not","haoo") == [1, 1, 4, 1]

    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
