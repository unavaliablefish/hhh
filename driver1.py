class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def buildTree(inorder , postorder ) :
        def help(inorder_left, inorder_right, postorder_right):
            if inorder_left > inorder_right:
                return None
            root_index = postorder_right
            root = TreeNode(postorder[root_index])

            inorder_root_index = idx_map[postorder[root_index]]
            size = inorder_root_index - inorder_left
            # print(root, size)
            root.left = help(inorder_left, inorder_root_index - 1,  postorder_right -  1- (inorder_right - inorder_root_index))
            root.right = help(inorder_root_index + 1, inorder_right,   postorder_right - 1)
            return root 


        
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        print(idx_map)
        return help(0, len(inorder) - 1, len(inorder) - 1)
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            # 将子节点加入队列，即使它们是None
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    
    # 清除尾部的None值，这些None不属于最后一层
    while result and result[-1] is None:
        result.pop()
    
    return result


# 测试用例
inorder = list(map(int,input().split(",")))
postorder = list(map(int,input().split(",")))

# 构建二叉树
root = buildTree(inorder, postorder)

# 获取层次遍历结果
result = level_order_traversal(root)
print(result)

