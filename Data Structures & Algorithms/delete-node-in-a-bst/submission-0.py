# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def MinChild(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # input: root (node), key (int)
        # output: root (node) (changed or possibly unchanged)

        # traverse through this BST, leveraging the properties of a BST to determine
        # whether or not this node with key exists!
        # if we don't find this node, return root (bst unchanged)
        # if we find this node, we need to proceed with removal
        # if removing...
        # node with no children
        # we just have to make sure that that node's parent is now pointing to nothing
        # node has one child
        # make sure that that's node parent's is now pointing to that child
        # if 2 children
        # find the smallest child of that node's right subtree (may require us to implement a helper function)

        if not root:
            return root
        print(f"current node: {root.val}")

        if root.val == key:
            print("value found!")
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else:
                min_child = self.MinChild(root.right)
                print(f"min_child: {min_child.val}")
                root.val = min_child.val
                root.right = self.deleteNode(root.right, min_child.val)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
        





