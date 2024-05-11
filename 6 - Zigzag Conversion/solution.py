# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cols_count = len(s)
        matrix = [["" for i in range(len(s))] for j in range(numRows)]
        k = 0

        if numRows == 1:
            return s

        for j in range(cols_count):
            for i in range(numRows):
                if j % (numRows-1) == 0 or (i+j) % (numRows-1) == 0:
                    matrix[i][j] = s[k] if k < len(s) else ""
                    k = k+1

        result = ""
        for i in range(numRows):
            for j in range(cols_count):
                result += matrix[i][j]
        return result

solution = Solution()
print(solution.convert("123456789", 3))