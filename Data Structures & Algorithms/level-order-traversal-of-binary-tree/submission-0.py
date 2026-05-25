# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        output = []

        if not root:
            return output

        queue.append(root)

        while len(queue) > 0:
            layer = []
            for i in range(len(queue)):
                current = queue.popleft()
                layer.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            output.append(layer)

        return output
