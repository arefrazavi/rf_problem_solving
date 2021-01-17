# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if not list1:
            return list2

        # Find the node before the node in a position
        node_before_a = self.find_node_by_pos(list1, a - 1)
        # Find the node after the node in b position
        # Used node_before_a to avoid searching the list from the beginning.
        node_after_b = self.find_node_by_pos(node_before_a, b - a + 2)

        # Append list2 to list2 from node a - 1 position.
        node_before_a.next = list2

        list2_last_node = list2
        # Find last node in list2.
        while list2_last_node.next:
            list2_last_node = list2_last_node.next

        # Prepend list2 to List1 from node b + 1 position.
        list2_last_node.next = node_after_b

        return list1

    def find_node_by_pos(self, head: ListNode, pos: int) -> ListNode:
        """
        Find the node in a specific position of the given.
        """
        i = 0
        node = head
        while i < pos and node.next:
            node = node.next
            i += 1

        return node
