class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):

    fast, slow = head, head

    while fast and fast.next:

        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    # a = ListNode(1)
    # b = ListNode(2)

    # a.next = b
    # b.next = None

    print(has_cycle(a))
