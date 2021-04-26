import functools


def strStr(t, s):
    # O(t*s) time is NOT optimal, rabin_karp below solves this in O(m+n)
    if s == "" or s == t:
        return 0

    for i in range(len(t)):
        if t[i] == s[0]:
            if len(t) - i < len(s):
                return -1
            for x in range(len(s)):
                if s[x] != t[i+x]:
                    break
                elif s[x] == t[i+x] and x == len(s)-1:
                    return i
    return -1


def strStr2(haystack, needle):
    if needle == "":
        return 0
    x = len(haystack.split(needle)[0])

    if len(haystack) != x:
        return x
    else:
        return -1


def rabin_karp(t, s):
    if len(s) > len(t):
        return -1

    BASE = 26

    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
    power_s = BASE**max(len(s)-1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i-len(s):i] == s:
            return i - len(s)

        t_hash -= ord(t[i-len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])


print(strStr("this was the first of the", "the"))
print(strStr("abc", "c"))
print(strStr("mississippi", "issipi"))
print(strStr("", "a"))

print(rabin_karp("abc abc thi this is me", "this"))
print(strStr2("mississipi", "issipi"))
