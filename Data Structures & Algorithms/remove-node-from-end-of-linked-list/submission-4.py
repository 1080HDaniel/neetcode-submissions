# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        poop = []
        node = head

        while node:
            poop.append(node)
            node = node.next

        target = poop[-n]

        if target == head:
            return head.next

        node = head
        while node:
            if node.next == target:
                node.next = target.next
                break
            node = node.next

        return head