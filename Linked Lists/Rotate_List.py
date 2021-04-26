class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def rotateRight(head, k):

    if head is None or head.next is None or k == 0:
        return head  # We have nothing to rotate in a 1 or 0 node linked-list

    # Find the length and last node of the linked-list

    last_node = head
    list_length = 1

    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    last_node.next = head
    k %= list_length
    skip_length = list_length - k
    lnorl = head

    for _ in range(skip_length - 1):
        lnorl = lnorl.next

    x = lnorl.next
    head = x
    lnorl.next = None

    return head


if __name__ == "__main__":

    print("-------------- \n")

    print(rotateRight(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).data)
    print(rotateRight(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.data)
    print(rotateRight(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.data)
    print(rotateRight(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.data)
    print(rotateRight(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.data)
    print(rotateRight(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.data)
    print(rotateRight(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.next.data)
    print(rotateRight(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3).next.next.next.next.next.next.next.data)
