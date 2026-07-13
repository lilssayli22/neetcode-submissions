# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        l={}
        def prof(root):
            if not root : 
                return 0
            a = prof(root.left)
            l[root.left] = a
            b = prof(root.right)
            l[root.right] = b
            l[root] = 1 + max(l[root.left],l[root.right])

            return l[root]
        prof(root)
        def final(root):
         if not root:
            return True
         if abs(l[root.right]-l[root.left])>1 : 
            return False
         else:
            return (True and final(root.left) and final(root.right))
        
        return final(root)
        

        
        