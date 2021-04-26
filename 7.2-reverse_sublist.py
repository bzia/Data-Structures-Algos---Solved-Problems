class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def reverse_sublist(head, left, right):

    dummy_head = sublist_head = ListNode(0, head)

    for i in range(1, left):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next

    for i in range(right - left):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next


# print(reverse_sublist(ListNode(1, ListNode(
#     2, ListNode(3, ListNode(4, ListNode(5))))), 3, 4).data)
# print(reverse_sublist(ListNode(1, ListNode(
#     2, ListNode(3, ListNode(4, ListNode(5))))), 3, 4).next.data)
# print(reverse_sublist(ListNode(1, ListNode(2, ListNode(
#     3, ListNode(4, ListNode(5))))), 3, 4).next.next.data)
# print(reverse_sublist(ListNode(1, ListNode(2, ListNode(
#     3, ListNode(4, ListNode(5))))), 3, 4).next.next.next.data)
# print(reverse_sublist(ListNode(1, ListNode(2, ListNode(
#     3, ListNode(4, ListNode(5))))), 3, 4).next.next.next.next.data)
