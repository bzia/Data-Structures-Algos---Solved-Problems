def custom_delete_duplicates(A):
    """
    Write a program which takes as input a sorted array and updates it so that all duplicates have been
    removed and the remaining elements have been shifted left to fill the emptied indices. Return the
    number of valid elements.

    CUSTOM SOLUTION BASED ON LEETCODE VARIATION: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    Time: O(n) 
    Space: O(1) 
    """
    if len(A) == 2:
        return 1 if A[0] == A[1] else 2

    front_ptr = 0
    back_ptr = len(A)-1

    while front_ptr < back_ptr:
        if A[front_ptr] == A[front_ptr + 1]:
            del A[front_ptr]
            back_ptr -= 1
        else:
            front_ptr += 1
    return len(A)


def custom_delete_duplicates(A):

    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index - 1] = A[i]
            write_index += 1

    return write_index
