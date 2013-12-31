def construct_failure_array(pattern):
    failure_array = [0] * (len(pattern) + 1)
    for i in xrange(2, len(failure_array)):
        last_val = failure_array[i - 1]
        while True:
            if pattern[last_val] == pattern[i - 1]:
                failure_array[i] = last_val + 1
                break
            if last_val == 0:
                failure_array[i] = 0
                break
            last_val = failure_array[last_val]

    return failure_array


def kmp(text, pattern, start_index=0):
    failure_array = construct_failure_array(pattern)
    j = 0
    m = len(pattern)
    i = start_index
    while True:
        if i >= len(text):
            break

        if text[i] == pattern[j]:
            j += 1
            i += 1
            if j == m:
                return i - m
        elif j > 0:
            j = failure_array[j]
        else:
            i += 1

    return -1