def naive_plus_one(A):
    """
    Write a program which takes as input an array of digits encoding a non-negative decimal integer D 
    and updates the array to represent the integer D + 1. For example, if the input is (1,2,9) then
    you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
    language that has finite-precision arithmetic.

    Time: O(n) - for stringifying each int in the array and for adding new ints into the new array
    Space: O(n) - creating the new array with the ints representing the incremented integer

    Note: will fail if A represents an integer larger than we can handle with python int type
    """
    for i in range(len(A)):
        A[i] = str(A[i])

    A = ''.join(A)
    A = int(A)
    A += 1
    A = str(A)

    new = []
    for num in A:
        new.append(int(num))

    return new


def plus_one_custom_optimal(digits):
    """
    Time: O(n) - for stringifying each int in the array and for adding new ints into the new array
    Space: O(1) - creating the new array with the ints representing the incremented integer
    """
    if digits[len(digits)-1] + 1 != 10:
        digits[len(digits)-1] += 1
        return digits

    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]

    else:
        nine_count = 0
        for i in reversed(range(1, len(digits))):
            if digits[i] == 9:
                nine_count += 1
                if digits[i-1] != 9:
                    break
                if digits[i-1] == 9 and i == 1:
                    nine_count += 1
                    break

    if nine_count == len(digits):
        digits[0] = 1
        for i in range(1, len(digits)):
            digits[i] = 0
        digits.append(0)
        return digits

    digits[len(digits)-nine_count-1] += 1
    for i in range(len(digits)-nine_count, len(digits)):
        digits[i] = 0

    return digits


def plus_one(A):
    """
    Time: O(n) - for stringifying each int in the array and for adding new ints into the new array
    Space: O(1) - creating the new array with the ints representing the incremented integer
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A.append(0)
        A[0] = 1

    return A


test = [9]
print(plus_one_custom_optimal(test))
