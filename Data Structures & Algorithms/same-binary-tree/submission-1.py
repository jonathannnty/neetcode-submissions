# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # two queues one for p and one for q
        if not p and q or p and not q:
            return False

        
        queue_p = deque()
        queue_q = deque()

        if p:
            queue_p.append(p)
        if q:
            queue_q.append(q)

        while len(queue_p) > 0:
            if len(queue_p) != len(queue_q):
                return False
            curr_p = queue_p.popleft()
            curr_q = queue_q.popleft()

            if curr_p.val != curr_q.val:
                return False
            
            if curr_p.left and not curr_q.left or not curr_p.left and curr_q.left:
                return False
            if curr_p.left:
                queue_p.append(curr_p.left)
                queue_q.append(curr_q.left)
            
            if curr_p.right and not curr_q.right or not curr_p.right and curr_q.right:
                return False
            if curr_p.right:
                queue_p.append(curr_p.right)
                queue_q.append(curr_q.right)
        return True
