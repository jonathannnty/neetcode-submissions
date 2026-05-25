# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # input: root > part of the bst
        # the node's values where the node is the right-most 
        # node in the bst
        # bfs, queue

        queue = deque()
        output = []

        if not root:
            return output
        
        queue.append(root)

        while len(queue) > 0:
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                print(f"queue: {queue}")
                print(f"current: {current.val}")
                if i == length - 1:
                    # we know that it's the right most
                    print(f"adding rightmost: {current.val}")
                    output.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return output
        