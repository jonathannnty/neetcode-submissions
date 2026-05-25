# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorderTraversal(root, k, None)[1]
    
    # left, current, right


    def inorderTraversal(self, node, k, val):
        if not node:
            return k, val
        print(f"node.val: {node.val}, k: {k}, val: {val}")
        k, val = self.inorderTraversal(node.left, k, val)

        k -= 1
        print(f"node.val: {node.val}, k: {k}, val: {val}")
        if k == 0 and val == None:
            return k, node.val

        k, val = self.inorderTraversal(node.right, k, val)
        
        return k, val

