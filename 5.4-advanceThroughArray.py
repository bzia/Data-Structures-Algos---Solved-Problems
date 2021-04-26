def can_reach_end(A):
    """
    Write a program which takes an array of n integers, where A[i] denotes the maximum you can
    advance from index i, and returns whether it is possible to advance to the last index starting from
    the beginning of the array.
    """

    last_index = len(A) - 1
    furthest_reached = 0
    i = 0

    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(A[i] + i, furthest_reached)
        i += 1

    return furthest_reached >= last_index


def custom_can_jump(A):

    last_index = len(A) - 1

    if A[0] == 0 and len(A) > 1:
        return False
    elif A[0] == 0 and len(A) == 1:
        return True

    i = 0
    while i < len(A):
        reach = i + A[i]

        if reach >= last_index:
            return True

        k = 1
        while k <= A[i] + 1:
            if A[i+k] > (A[i] - k):
                i = i + k
                if i == last_index:
                    return True
                break
            elif A[i+k] == 0 and (A[i] - k) == 0:
                return False
            else:
                k += 1


def can_jump(nums):
    # LEETCODE VARIATION: https://leetcode.com/problems/jump-game/
    minimum_jump = 1

    for i in reversed(range(len(nums)-1)):
        if nums[i] >= minimum_jump:
            minimum_jump = 1
        else:
            minimum_jump += 1

    if nums[0] >= minimum_jump or len(nums) == 1:
        return True
    else:
        return False


print(can_reach_end([1, 0, 3, 4, 0, 6, 7]))
print(can_jump([3, 2, 2, 0, 4]))
