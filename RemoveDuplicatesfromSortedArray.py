class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_list = nums[:]
        k = 1
        count = 0
        current = nums[0]

        for index in range(len(nums)-1):

            if current == nums_list[index+1]:
                nums[-1-count] = '_'
                count += 1
            elif current < nums_list[index+1]:
                nums[k] = nums_list[index+1]
                current = nums[k]
                k += 1

        return k, nums


if __name__ == "__main__":

    nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    print(Solution().removeDuplicates(nums))
