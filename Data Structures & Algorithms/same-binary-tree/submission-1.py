# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pee = deque([p])
        qoo = deque([q])

        while pee:
            node1 = pee.popleft()
            node2 = qoo.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            pee.append(node1.left)
            pee.append(node1.right)

            qoo.append(node2.left)
            qoo.append(node2.right)

        return True