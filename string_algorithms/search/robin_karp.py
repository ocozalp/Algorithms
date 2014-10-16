mod = 2 ** 31
b = 32


def calculate_h(t, start, end):
    h = 0
    mul = 1

    for i in xrange(end, start - 1, -1):
        s = (ord(t[i]) * mul) % mod
        h = (h + s) % mod
        mul = (mul * b) % mod

    return h


def re_calculate_h(text, h, b_max, index, new_index):
    new_h = h - (ord(text[index - 1]) * b_max)
    new_h *= b
    new_h += ord(text[new_index])
    new_h %= mod

    return new_h


def get_b_max(count):
    result = 1
    for i in xrange(count):
        result = (result * b) % mod

    return result


def rabin_karp(text, pattern, start_index=0):
    pattern_h = calculate_h(pattern, 0, len(pattern) - 1)
    h = -1
    b_max = get_b_max(len(pattern) - 1)

    for i in xrange(start_index, len(text) - len(pattern) + 1):
        if i == start_index:
            h = calculate_h(text, start_index, start_index + len(pattern) - 1)
        else:
            h = re_calculate_h(text, h, b_max, i, i + len(pattern) - 1)

        if h == pattern_h:
            found = True
            for j in xrange(len(pattern)):
                if text[i + j] != pattern[j]:
                    found = False
                    break

            if found:
                return i

    return -1
