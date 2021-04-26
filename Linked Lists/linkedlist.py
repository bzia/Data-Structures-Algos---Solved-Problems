class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def search_list(self, L, key):
    while L and L.data != key:
        L = L.next

    return L


def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


def delete_after(self, node):
    node.next = node.next.next

#########################################################


def test():

    ll = ListNode(1, ListNode(2, ListNode(
        3, ListNode(4, ListNode(5, ListNode(6))))))
    print(ll.data)
    print(ll.next.data)
    print(ll.next.next.data)
    print(ll.next.next.next.data)
    print(ll.next.next.next.next.data)
    print(ll.next.next.next.next.next.data)

    insert_after(ll, ListNode(9))
    print("-------")

    print(ll.data)
    print(ll.next.data)
    print(ll.next.next.data)
    print(ll.next.next.next.data)
    print(ll.next.next.next.next.data)
    print(ll.next.next.next.next.next.data)
    print(ll.next.next.next.next.next.next.data)

    nodeA = ListNode(1)
    nodeB = ListNode(2)
    nodeC = ListNode(3)
    nodeD = ListNode(4)

    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD


test()

#########################################################
