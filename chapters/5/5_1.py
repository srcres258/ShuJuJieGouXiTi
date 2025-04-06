"""
以二叉链表作为二叉树的存储结构，设计以下算法：

1. 统计二叉树的叶子节点个数。
2. 设计二叉树的双序遍历算法（双序遍历是指对于二叉树的每一个结点来说，先访问这个结点，再按双序遍历它的左子树，然后再一次访问这个结点，接下来按双序遍历它的右子树）。
3. 用按层次顺序遍历二叉树的方法，统计树中度为1的结点数目。
"""


from collections import deque


class Node:
    """
    二叉树节点
    """

    def __init__(self, val=None, left=None, right=None):
        self.val: int | None = val
        self.left: Node | None = left
        self.right: Node | None = right


def count_leaf_nodes(root: Node) -> int:
    """
    统计二叉树的叶子节点个数
    """

    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


def double_order_traversal(root: Node) -> None:
    """
    二叉树的双序遍历算法
    """

    if root is None:
        return
    print(root.val, end=' ') # 先访问当前结点
    double_order_traversal(root.left) # 再按双序遍历它的左子树
    print(root.val, end=' ') # 再访问当前结点
    double_order_traversal(root.right) # 最后按双序遍历它的右子树


def count_nodes_with_degree_one(root: Node) -> int:
    """
    统计树中度为1的结点数目
    """

    if root is None:
        return 0
    queue = deque([root])
    count = 0
    while queue:
        node = queue.popleft()
        if (node.left and not node.right) or (node.right and not node.left):
            count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count