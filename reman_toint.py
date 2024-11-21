class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        temp = -1
        str_list = list(s)

        for char in str_list:
            if char == "I":
                count = 1
            elif char == "V":
                count = 5
            elif char == "X":
                count = 10
            elif char == "L":
                count = 50
            elif char == "C":
                count = 100
            elif char == "D":
                count = 500
            elif char == "M":
                count = 1000
            else:
                continue

            if count/temp == 5 or count/temp == 10:
                count -= 2 * temp
                temp = -1
            else:
                temp = count

            result += count
            count = 0

        return int(result)


if __name__ == "__main__":
    s = "MCMXCIV"
    print(Solution().romanToInt(s))
