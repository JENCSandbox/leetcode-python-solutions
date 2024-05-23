class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        for i in range(len(nums)):
            temp.append((nums[i], i))

        temp = list(sorted(temp, key=lambda pair: pair[0]))

        left = 0
        right = len(temp) - 1

        result = []

        while left < len(temp) and right >= 0:
            # print('left: ' + str(left) + ' ' + ' right: ' + str(right))
            sum_left_right = temp[left][0] + temp[right][0]
            if sum_left_right == target:
                result.append(temp[left][1])
                result.append(temp[right][1])
                break
            elif sum_left_right < target:
                left += 1
            else:
                # sum_left_right > target:
                right -= 1
        return result


sol = Solution()

print(sol.twoSum([-1, -2, -3, -4, -5], -8))
print(sol.twoSum([150, 24, 79, 50, 88, 345, 3], 200))
