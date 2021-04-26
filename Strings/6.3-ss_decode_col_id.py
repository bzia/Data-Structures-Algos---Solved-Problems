import functools


def ss_decode_col_id(col):

    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)

# Custom Leetcode Solution


def titleToNumber(columnTitle):
    result = 0
    for i in range(len(columnTitle)):
        result += (ord(columnTitle[len(columnTitle) - i - 1]) - 64) * 26 ** i

    return result


col = "AAA"
print(titleToNumber(col))


col = "AAA"
print(titleToNumber(col))
print(ss_decode_col_id(col))
