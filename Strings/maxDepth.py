def maxDepth(s):
    oc, max_depth = 0, 0

    for i in range(len(s)):
        if s[i] == "(":
            oc += 1
            max_depth = max(oc, max_depth)
        elif s[i] == ")":
            oc -= 1

    return max_depth


print(maxDepth("(1+(2*3)+((8)/4))+1"))  # 3
