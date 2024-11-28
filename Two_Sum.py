class Solution(object):
    def twoSum(self, nums, target):
        import numpy as np
        import math
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = np.array([], dtype=int)

        my_nums = np.array([nums, np.argsort(nums)])

        for i in range(len(nums)):
            low = my_nums[0, i]

            count = 0
            j = math.ceil(len(my_nums[0, i+1:])/2+0.1) + i

            while np.size(result) == 0:
                print(j)
                high = my_nums[0, j]

                if low + high == target:
                    result = np.append(result, [int(i), int(j)])
                    break
                elif low + high > target:
                    j -= 1
                    count += 1
                elif low + high < target:
                    j += 1
                    count -= 1

                if abs(count) in [0, 2]:
                    break

            if np.size(result) == 2:
                break

        return result.tolist()


# def main():
#     solution = Solution()
#     print(solution.twoSum([2, 7, 11, 15], 9))  # 輸出：[0, 1]
#     print(solution.twoSum([3, 2, 4], 6))  # 輸出：[1, 2]
#     print(solution.twoSum([3, 3], 6))  # 輸出：[0, 1]

if __name__ == "__main__":
    num_list = [[2, 7, 11, 15], 9]
    print(Solution().twoSum(num_list[0], num_list[1]))

