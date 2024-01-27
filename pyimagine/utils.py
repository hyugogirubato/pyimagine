import random


def purify(value: str) -> str:
    chars = list(value)
    size = len(chars) - 1
    vowel = chars[0] in 'aeiouy'

    for i in range(size + 1):
        if i > 0 and chars[i] == chars[i - 1]:
            chars.insert(i + 1, chars[i])
            return "".join(chars)
        if i == size // 2 and size % 2 == 1:
            chars.insert(i + 1, chars[i])
            return "".join(chars)

    if vowel:
        chars.insert(2, chars[1])
    else:
        i = random.randint(0, size)
        chars.insert(i + 1, chars[i])
    return ''.join(chars)
