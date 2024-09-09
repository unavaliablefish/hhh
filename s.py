from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]

            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root
 
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

    def levelOrderTraversal(self, root):
        result = []
        if not root:
            return result
 
        queue = deque([root])
 
        while queue:
            current_level = []
            next_level = deque() 
            for node in queue:
                if node:
                    current_level.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    current_level.append(None)
                    next_level.append(None)
                    next_level.append(None)
            if any(current_level):
                result.append(current_level)
            if not any(next_level):
                break
            queue = next_level

        return result


inorder = list(map(int,input().split(',')))
postorder = list(map(int,input().split(',')))

solution = Solution()
result = solution.buildTree(inorder, postorder)



a=solution.levelOrderTraversal(result)
while a[-1] and a[-1][-1] is None:
     a[-1].pop()



result_str = ', '.join(['null' if item is None else str(item) for sublist in a for item in sublist])

print(result_str)