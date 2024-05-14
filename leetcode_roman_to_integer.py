class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        DICT_SYMBOL = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        reverse_s = s[::-1]
        for i in range(len(reverse_s)):
            if i > 0 and (
                DICT_SYMBOL[reverse_s[i]] < DICT_SYMBOL[reverse_s[i-1]]
            ):
                result -= DICT_SYMBOL[reverse_s[i]]
            else:
                result += DICT_SYMBOL[reverse_s[i]]
        return result


s = Solution()
print(s.romanToInt('XIX'))
