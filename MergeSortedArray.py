class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            # print(f"m={m}, n={n}, {nums1}")

        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1

        return nums1


if __name__ == "__main__":

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    print(Solution().merge(nums1, m, nums2, n))
