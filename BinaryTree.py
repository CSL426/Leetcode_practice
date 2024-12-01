# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0  # 如果節點為空，深度為0

        # 遞歸計算左子樹和右子樹的深度，取其中較大的一個加1
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

# 創建二叉樹的函數


def create_tree(nodes):
    if not nodes:
        return None

    # 創建節點列表
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        node = queue.pop(0)
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    # 樹的表示方式為一個列表，None 表示沒有節點
    root = [3, 9, 20, None, None, 15, 7]
    tree_root = create_tree(root)
    print(Solution().maxDepth(tree_root))
