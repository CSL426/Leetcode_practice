class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    s = "()"
    print(Solution().isValid(s))
