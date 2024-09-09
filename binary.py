class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(level_order):
    if not level_order:
        return None
    root = TreeNode(level_order[0])
    queue = [root]
    i = 1
    while i < len(level_order):
        current = queue.pop(0)
        if current:
            if i < len(level_order) and level_order[i] is not None:
                current.left = TreeNode(level_order[i])
                queue.append(current.left)
            i += 1
            if i < len(level_order) and level_order[i] is not None:
                current.right = TreeNode(level_order[i])
                queue.append(current.right)
            i += 1
    return root

def prune_tree(root):
    if not root:
        return None
    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)
    if root.value == 0 and not root.left and not root.right:
        return None
    return root

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left if current.left or (current.left is None and current.right) else None)
            queue.append(current.right if current.right else None)
        else:
            result.append(None)
    # 去除尾部的None，这些None不属于最后一层
    while result and result[-1] is None:
        result.pop()
    return result

# 示例输入
level_order = [1, 0, 1, 0, 0, 0, 1]

# 构建二叉树
root = build_tree(level_order)

# 剪枝操作
root = prune_tree(root)

# 获取层次遍历结果
result = level_order_traversal(root)
print(result)