class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    x = 1314
    print(Solution().isPalindrome(x))
