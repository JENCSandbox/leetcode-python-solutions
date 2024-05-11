# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        cols_count = 0
        matrix = []

        i = 0

        temp_sub_list = []

        for letter in s:
            if cols_count % (numRows-1) == 0 or (i+cols_count) % (numRows-1) == 0:
                temp_sub_list.append(letter)
            else:
                temp_sub_list.append("")

            if len(temp_sub_list) == numRows:
                matrix.append(temp_sub_list)
                temp_sub_list = []
                cols_count += 1






        result = ""

        return result

solution = Solution()
print(solution.convert("123456789", 3))