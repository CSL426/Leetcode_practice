class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Hint: startswith -> find str in s (defaut start with 0) and return true or false

        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 1:
            return strs[0]

        str = strs[0]

        for s in strs[1:]:
            while not s.startswith(str):
                str = str[:-1]
            if not str:
                return str

        return str


if __name__ == "__main__":
    strs = ["dog", "racecar", "car"]
    # strs = ["flower", "flow", "flight"]
    # strs = ["ab", "a"]
    # strs = ["reflower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
