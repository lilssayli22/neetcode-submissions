# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        rescent = root ;
        def f(root,rescent) : 
            x =0
            if root.left !=None : 
                if root.left.val >= rescent.val :
                    x =  1 + f(root.left,root.left)
                else : 
                    x += f(root.left,rescent)
            if root.right != None : 
                if root.right.val >= rescent.val:
                    
                    x+=1 + f(root.right,root.right)
                else :
                    x+= f(root.right,rescent)
            return x
        m= f(root,rescent)
        return m+1         
                