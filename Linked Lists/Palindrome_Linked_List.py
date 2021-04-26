class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def isPalindrome(head):

    if head is None or head.next is None:
        return True

    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    second_half = reverse(slow)

    while second_half:
        # If node values arent the same, the linked list not a palindrome
        if head.data != second_half.data:
            return False
        head = head.next
        second_half = second_half.next

    # All node values in the first half of the list and the revesed second half are equal
    return True


def reverse(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(3)
    e = ListNode(2)
    f = ListNode(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = None

    print(isPalindrome(a))
