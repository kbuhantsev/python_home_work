
import random


def code_decode(word, key, coding=True):

    chars_map = {ord(char): char for char in ''.join([chr(i) for i in range(32, 55296)])}
    translation_map = {}

    ind = 0
    for i in range(0, len(word)-1):

        trans_key = ord(key[ind]) + ind + len(key)

        try:
            if coding:
                translation_map[ord(word[i])] = chars_map[ord(word[i]) + trans_key]
            else:
                translation_map[ord(word[i])] = chars_map[ord(word[i]) - trans_key]
        except KeyError:
            translation_map[ord(word[i])] = random.randint(32, 55296)

        if ind == len(key)-1:
            ind = 0
        else:
            ind += 1
    return word.translate(translation_map)


coded = code_decode("абракадабра", "секретный ключ")
print(coded)
print(code_decode(coded, "секретный ключ", False))
print(f"{'*'*16}")
print(code_decode(coded, "секретныйключ", False))
print(code_decode(coded, "1111111", False))
print(code_decode(coded, "0", False))




