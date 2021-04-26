def balancedStringSplit(s):
    max, L, R = 0, 0, 0

    for i in range(len(s)):
        if s[i] == 'R':
            if L < 0:
                L += 1
                if L == 0:
                    max += 1
            else:
                R -= 1
        else:
            if R < 0:
                R += 1
                if R == 0:
                    max += 1
            else:
                L -= 1
    return max


def lc_shorter(s):
    max, c = 0, 0

    for char in s:
        if char == 'L':
            c += 1
        if char == 'R':
            c -= 1
        if c == 0:
            max += 1

    return max


print(balancedStringSplit("RLLLLRRRLR"))
print(lc_shorter("RLLLRRRL"))
