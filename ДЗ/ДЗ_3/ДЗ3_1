
def code(word, key):

    result = ""
    ind = len(key) - 1
    for symbol in word:
        result += chr(ord(symbol) + ord(key[ind]))
        if ind == 0:
            ind = len(key) - 1
        else:
            ind -= 1

    return result


def decode(word, key):

    result = ""
    ind = len(key) - 1
    for symbol in word:
        result += chr(ord(symbol) - ord(key[ind]))
        if ind == 0:
            ind = len(key) - 1
        else:
            ind -= 1

    return result


coded = code("python", "key")
print(coded)
print(decode(coded, "key"))


