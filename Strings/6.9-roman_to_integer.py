import functools


def romanToint(s):

    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sub = [9, 90, 900, 4, 40, 400]
    result = 0

    if len(s) == 1:
        return T[s[0]]

    i = 0
    while i < len(s)-1:
        if (T[s[i+1]] - T[s[i]]) in sub:
            result += T[s[i+1]] - T[s[i]]
            i += 2
            if i == len(s)-1:
                result += T[s[i]]
        else:
            result += T[s[i]]
            i += 1
            if i == len(s)-1:
                result += T[s[i]]

    return result


def roman_to_integer(s):

    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]),
        reversed(range(len(s)-1)), T[s[-1]])


print(roman_to_integer("MDCXCV"))
