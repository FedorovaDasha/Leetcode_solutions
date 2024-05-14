class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = digits
        length = len(result)

        if result[length-1] < 9:
            result[length-1] += 1
        else:
            result[length-1] = 0
            if length == 1:
                result.insert(0, 1)
            else:
                result[length-2] += 1
        return result


s = Solution()
print(s.plusOne([9]))
