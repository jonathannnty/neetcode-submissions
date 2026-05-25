# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and not subRoot or not root and subRoot:
            return False

        root_q = deque()
        root_q.append(root)

        while len(root_q) > 0:
            curr = root_q.popleft()

            if curr.val == subRoot.val:
                if self.isSameTree(curr, subRoot):
                    return True
            if curr.left:
                root_q.append(curr.left)
            if curr.right:
                root_q.append(curr.right)
        return False

    def isSameTree(self, node1, node2):
        root_q = deque()
        subroot_q = deque()

        root_q.append(node1)
        subroot_q.append(node2)
        while len(subroot_q) > 0:
            curr = root_q.popleft()
            subcurr = subroot_q.popleft()
            if curr.val != subcurr.val:
                return False
            
            if not curr.left and subcurr.left or curr.left and not subcurr.left:
                return False
            if curr.left:
                root_q.append(curr.left)
                subroot_q.append(subcurr.left)
            
            if not curr.right and subcurr.right or curr.right and not subcurr.right:
                return False
            if curr.right:
                root_q.append(curr.right)
                subroot_q.append(subcurr.right)
        return True
        