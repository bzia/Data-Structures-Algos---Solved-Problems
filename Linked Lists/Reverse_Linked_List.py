class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def reverse_list(head):
    # LC easy variation: 'Reverse Linked List' (reverse whole list, not sublist (like in EPI))
    # Time: O(n), Space: O(1)

    cur = head
    prev = None

    while cur:
        nextTemp = cur.next
        cur.next = prev
        prev = cur
        cur = nextTemp

    return prev

# print(reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))).data)
# print(reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))).next.data)
# print(reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))).next.next.data)
# print(reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))).next.next.next.data)
