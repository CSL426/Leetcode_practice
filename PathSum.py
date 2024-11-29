# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False

        path_val = root.val

        # 如果是葉子結點 直接比較
        if not root.left and not root.right:
            return path_val == targetSum

        left_path = self.hasPathSum(root.left, targetSum-path_val)
        right_path = self.hasPathSum(root.right, targetSum-path_val)

        return left_path or right_path


def create_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]

    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root


if __name__ == "__main__":
    # 樹的表示方式為一個列表，None 表示沒有節點
    null = None
    root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]
    targetSum = 22

    # root = [1, 2, 3]
    # targetSum = 5

    # root = [1, 2]
    # targetSum = 0

    tree_root = create_tree(root)
    print(Solution().hasPathSum(tree_root, targetSum))
