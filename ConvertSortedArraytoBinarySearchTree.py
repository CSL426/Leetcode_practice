# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def create_tree(left, right):
            # 終止條件：左邊界大於右邊界
            if left > right:
                return None

            # 計算中間點
            mid = (left + right) // 2

            # 建立節點
            root = TreeNode(nums[mid])

            # 遞迴建立左右子樹
            root.left = create_tree(left, mid - 1)
            root.right = create_tree(mid + 1, right)

            return root

        return create_tree(0, len(nums) - 1)


def print_tree_structure(root, level=0, prefix="Root: "):
    if root is not None:
        print("  " * level + prefix + str(root.val))
        if root.left or root.right:
            print_tree_structure(root.left, level + 1, "L--- ")
            print_tree_structure(root.right, level + 1, "R--- ")


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    tree_root = solution.sortedArrayToBST(nums)
    print_tree_structure(tree_root)
