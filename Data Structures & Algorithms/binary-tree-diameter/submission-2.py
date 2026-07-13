class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        memo = {}

        def prof(node):
            if node is None:
                return -1
            if node in memo:
                return memo[node]
            result = 1 + max(prof(node.left), prof(node.right))
            memo[node] = result
            return result

        def f(node, loop):
            if node is None:
                return 0
            if not loop:
                return prof(node)
            else:
                option_ici = 2 + prof(node.left) + prof(node.right)
                option_gauche = f(node.left, True)
                option_droite = f(node.right, True)
                return max(option_ici, option_gauche, option_droite)

        return f(root, True)