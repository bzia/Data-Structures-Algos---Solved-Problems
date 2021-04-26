class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def reverse_every_k_elements(head, k):
    # Variation: Reverse remaining nodes at the end even if there arent enough to form a k-group
    # GROKKING's own solution

    if k <= 1 or head is None:
        return head

    current, prev = head, None

    while True:

        lnp = prev
        lns = current
        next = None

        i = 0
        while current is not None and i < k:

            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1

        if lnp is not None:
            lnp.next = prev
        else:
            head = prev

        lns.next = current

        if current is None:
            break

        prev = lns

    return head


def reverseKGroup(head, k):
    # LC HARD Variation
    # Variation: Dont reverse remaining nodes

    dummy = jump = ListNode(0, head)
    left = right = head

    while True:

        count = 0

        while right and count < k:
            right = right.next
            count += 1

        if count == k:
            prev, cur = right, left

            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            jump.next = prev
            jump = left
            left = right

        else:
            return dummy.next


def reverseKGroup_Grokking(head, k):
    # My altered LC solution to conform to Grokkings variation
    # I took the LC solution and added code to reverse the remaining nodes found starting at pointer 'left'

    dummy = jump = ListNode(0, head)
    left = right = head

    while True:

        count = 0

        while right and count < k:
            right = right.next
            count += 1

        if count == k:
            prev, cur = right, left

            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            jump.next = prev
            jump = left
            left = right

        else:
            prev = None
            while left:
                temp = left.next
                left.next = prev
                prev = left
                left = temp
            # link the node which pointed to the remaining nodes
            # that were too small to form the k-group
            jump.next = prev
            break

    return dummy.next


if __name__ == "__main__":

    print("--------------")

    print("Testing Grokking's Solution")

    print(reverse_every_k_elements(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).data)
    print(reverse_every_k_elements(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.data)
    print(reverse_every_k_elements(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.data)
    print(reverse_every_k_elements(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.data)
    print(reverse_every_k_elements(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.data)
    print(reverse_every_k_elements(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.data)
    print(reverse_every_k_elements(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.next.data)
    print(reverse_every_k_elements(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.next.next.data)

    print("\nTesting LC Variation (DO NOT reverse remaining portion if its smaller than a k-group) \n")

    print(reverseKGroup(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).data)
    print(reverseKGroup(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.data)
    print(reverseKGroup(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.data)
    print(reverseKGroup(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.data)
    print(reverseKGroup(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.data)
    print(reverseKGroup(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.data)
    print(reverseKGroup(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.next.data)
    print(reverseKGroup(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.next.next.data)

    print("\nTesting custom modified LC variation that matches grokking's problem setting \n")

    print(reverseKGroup_Grokking(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).data)
    print(reverseKGroup_Grokking(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.data)
    print(reverseKGroup_Grokking(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.data)
    print(reverseKGroup_Grokking(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.data)
    print(reverseKGroup_Grokking(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.data)
    print(reverseKGroup_Grokking(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.data)
    print(reverseKGroup_Grokking(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.next.data)
    print(reverseKGroup_Grokking(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.next.next.data)
