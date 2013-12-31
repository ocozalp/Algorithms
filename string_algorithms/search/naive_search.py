def naive_search(text, pattern, start_index=0):
    for i in xrange(start_index, len(text) - len(pattern) + 1):
        found = True
        for j in xrange(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return i

    return -1