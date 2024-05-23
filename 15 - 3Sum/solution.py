class Solution(object):
    def threeSum(self, nums):

        def different_values(x, y, z):
            return x != y and x != z and y != z

        def is_present(x, y, z, lists):
            present = False
            for sub_list in lists:
                if set(sub_list) == {x, y, z}:
                    present = True
                    break
            return present

        sorted_nums = list(sorted(nums))
        length_of_nums = len(sorted_nums)
        result = []

        for a in range(length_of_nums-1):
            if a + 1 < len(sorted_nums):
                left = a + 1
                right = length_of_nums - 1

                while left < length_of_nums and right > a and left < right:
                    three_sum = sorted_nums[a] + sorted_nums[left] + sorted_nums[right]
                    if three_sum == 0:
                        if different_values(a, left, right) and not is_present(sorted_nums[a], sorted_nums[left], sorted_nums[right], result):
                            result.append([sorted_nums[a], sorted_nums[left], sorted_nums[right]])
                        left += 1
                        right -= 1
                    elif sorted_nums[left] + sorted_nums[right] < -1*sorted_nums[a]:
                        left += 1
                    else:
                        # sum_left_right > target:
                        right -= 1
        return result
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]
print(sol.threeSum([0, 1, 1])) #[]
print(sol.threeSum([0, 0, 0])) #[[0, 0, 0]]
print(sol.threeSum([-2, 0, 1, 1, 2]))
print(sol.threeSum([0, 0, 0, 0])) #[[0, 0, 0]]

