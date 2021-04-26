"""Example of O(1) space solution to problem where you want to put the even
numbers at the start of the list. Performed a 3-way partition of list.

The goal was to show that we dont need a new array which would have made the 
space complexity O(n)
"""


def evenOdd(lis):

    next_even = 0
    next_odd = len(lis) - 1

    while next_even < next_odd:
        if lis[next_even] % 2 == 0:
            next_even += 1
        else:
            lis[next_even], lis[next_odd] = lis[next_odd], lis[next_even]
            next_odd -= 1

    return lis


tst = [1, 3, 4, 5, 6, 7, 8, 9]
print(evenOdd(tst))
