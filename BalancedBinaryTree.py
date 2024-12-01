# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def height(root):
            if not root:
                return 0

            left_depth = height(root.left)

            right_depth = height(root.right)

            if (abs(left_depth-right_depth) > 1
                    or right_depth == -1
                    or left_depth == -1):
                return -1

            return max(left_depth, right_depth) + 1

        return height(root) != -1


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
    print(Solution().isBalanced(tree_root))
