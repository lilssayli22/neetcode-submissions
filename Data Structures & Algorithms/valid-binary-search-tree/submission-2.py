class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        r = None
        l = None
        def valide_sons(root, r, l):
            x = True
            y = True
            if root == None:
                return True
            if (r == None) and (l == None):
                return x and y and valide_sons(root.right, root, l) and valide_sons(root.left, r, root)
            else:
                if l == None:
                    x = (root.val > r.val)
                    return x and y and valide_sons(root.right, root, l) and valide_sons(root.left, r, root)
                elif r == None:
                    y = (root.val < l.val)
                    return x and y and valide_sons(root.right, root, l) and valide_sons(root.left, r, root)
                else:
                    x = (root.val > r.val)
                    y = (root.val < l.val)
                    return x and y and valide_sons(root.right, root, l) and valide_sons(root.left, r, root)
        return valide_sons(root, r, l)