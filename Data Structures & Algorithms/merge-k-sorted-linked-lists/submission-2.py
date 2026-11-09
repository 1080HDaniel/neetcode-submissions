# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        john = ListNode()
        array = []

        for llist in lists:
            while llist:
                array.append(llist.val)
                llist = llist.next
        array.sort()
        head = john

        for i in range(len(array)):
            john.val = array[i]
            if i < len(array)-1:
                node = ListNode()
                john.next = node
                john = john.next
        if head.val == 0 and head.next == None:
            return None
        return head
