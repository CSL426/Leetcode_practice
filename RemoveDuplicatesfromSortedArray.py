class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums = [1, 1, 2]

    print(Solution().removeDuplicates(nums))
