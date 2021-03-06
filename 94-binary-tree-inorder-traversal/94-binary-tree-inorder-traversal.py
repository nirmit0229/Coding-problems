# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if root!=None:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
            return arr
        arr = []
        return inorder(root)