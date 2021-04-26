def middleNode(head):

    fast, slow = head, head

    while fast and fast.next:
        fast = fast = fast.next.next
        slow = slow.next

    return slow
