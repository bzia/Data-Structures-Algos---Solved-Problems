class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def detectCycle(head):

    # Set 2 pointers; 'Fast' will advance at 2x the speed of 'Slow'
    fast, slow = head, head

    # Detect the Cycle (if no cycle, else block is hit, returning None)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    else:
        return None

    # Cycle is confirmed at this point, and we move 'head' to start of the cycle
    while head is not slow:
        head = head.next
        slow = slow.next

    return head


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

    print(detectCycle(a))
