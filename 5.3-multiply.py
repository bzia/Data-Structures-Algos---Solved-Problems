def multiply(num1, num2):
    """
    Write a program that takes two arrays representing integers, and returns an 
    integer representing their product

    Time: O(nm) 
    Space: O(n+m) 
    """
    # Firstly, the resulting array requires at most n + m digits for operands of n digits and m digits,
    # that is [n1,n2,n3] and [m1,m2,m3,m4] would require at most 7 digits to represent

    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1

    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += (result[i + j + 1] // 10)
            result[i + j + 1] %= 10

    # 'Removing Leading Zeroes' - From EPI
    # result = result[next((i for i, x in enumerate(
    #     result) if x != 0), len(result)):] or [0]

    # we will have at most 1 leading zero so we can check for and remove it
    if result[0] == 0:
        result.remove(result[0])

    return [sign * result[0]] + result[1:]


t1 = [-1]
t2 = [-4, 7, 3]
print(multiply(t1, t2))
