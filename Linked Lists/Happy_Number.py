def isHappy(n):
    # Time Complexity: O(log N)
    # Space Complexity: O(1)

    slow, fast = n, n
    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        if slow == fast:
            break

    return slow == 1


def find_square_sum(n):
    sums = 0

    while n > 0:
        digit = n % 10
        sums += digit * digit
        n //= 10

    return sums


if __name__ == "__main__":

    print(isHappy(23))
    # should be True since... 2^3 + 3^2 = 13 THEN 1^2 + 3^2 = 10 THEN 1^2 + 0^2 = 1
