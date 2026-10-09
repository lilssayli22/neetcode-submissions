# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def TreeToList(root):
            if root == None : 
                return []
            else :
                return TreeToList(root.left)+[root.val] + TreeToList(root.right)
        

        l = TreeToList(root)
        return l[k-1]