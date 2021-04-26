def naive_dutch_flag_partition(A, pivot_index):
    # Trivial Implementation
    # Time: O(n)
    # Space: O(n)
    pivot = A[pivot_index]
    new = []
    new.append(pivot)
    A.remove(pivot)

    for i in range(len(A)):
        if A[i] == pivot:
            new.insert(new.index(pivot) + 1, A[i])
        elif A[i] > pivot:
            new.append(A[i])
        else:
            new.insert(0, A[i])

    return new


def brute_dutch_flag_partition(A, pivot_index):
    # Time: O(n^2)
    # Space: O(1)
    pivot = A[pivot_index]

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

    return A


def optimal_dutch_flag_partition(A, pivot_index):
    # Time: O(n)
    # Space: O(1)
    # First loop put elements as less than pivot at the start
    # Second loop keeps track of the index 1 to the left of the last known element bigger than pivot and
    # if the loop finds an element larger than pivot, it will swap with the item 1 left of the last known item bigger than pivot
    pivot = A[pivot_index]

    smaller = 0
    for i in range(len(A)):

        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


def dutch_flag_partition(A, pivot_index):
    # While Loop Implementation
    # Time: O(n)
    # Space: O(1)
    pivot = A[pivot_index]

    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


def sort_colors(A):
    """LC Medium Variation"""

    l = len(A) - 1
    s = 0
    e = 0

    while e <= l:
        if A[e] < 1:
            A[s], A[e] = A[e], A[s]
            s += 1
            e += 1
        elif A[e] == 1:
            e += 1
        else:
            A[e], A[l] = A[l], A[e]
            l -= 1


test = [1, 4, 4, 6, 4, 1, 5, 7]
print(dutch_flag_partition(test, 2))
