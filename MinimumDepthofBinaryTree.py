# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Hint: BFS
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if not root.right:
            return left_depth + 1

        if not root.left:
            return right_depth + 1

        return min(left_depth, right_depth) + 1


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
    root = [3, 9, 20, null, null, 15, 7]
    # root = [2, null, 3, null, 4, null, 5, null, 6]
    tree_root = create_tree(root)
    print(Solution().minDepth(tree_root))
