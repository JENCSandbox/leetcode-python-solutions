from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        temp = n
        value = 1

        if n == 1:
           return [0]

        elif n % 2 != 0:
            result.append(0)
            temp -= 1

        while temp != 0:
            result.append(value)
            result.append(-value)
            temp -= 2
            value += 1

        return result

sol = Solution()
print(sol.sumZero(5))



