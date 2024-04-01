
class Solution(object):

    def getLastMoment(self, n, left, right):
        t = 0
        if len(left) > 0:
            t = max(left)
        if len(right) > 0:
            t = max(t, n-min(right))
        return t

solution = Solution()
print(solution.getLastMoment(4, [4, 3], [0, 1]))
print(solution.getLastMoment(7, [], [0, 1, 2, 3, 4, 5, 6, 7]))
print(solution.getLastMoment(7, [0, 1, 2, 3, 4, 5, 6, 7], []))

