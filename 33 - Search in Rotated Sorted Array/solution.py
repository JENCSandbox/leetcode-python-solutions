from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)  # size of numbers
        l, r = 0, n - 1
        rotated = False

        if n == 1: return 0 if nums[0] == target else -1

        # array is rotaded
        if (nums[l] > nums[r]):
            rotated = True
            print('rotaded')
            while True:
                h = (l + r) // 2
                if l + 1 == r and nums[l] > nums[r]:
                    break
                if nums[h] > nums[r]:
                    l = h
                elif nums[h] < nums[r]:
                    r = h
        if rotated:
            if nums[0] <= target <= nums[l]:
                print('left')
                r = l
                l = 0
            elif nums[r] <= target <= nums[n - 1]:
                print('right')
                l = r
                r = n - 1
            else:
                return -1
        print(l)
        print(r)
        while l + 1 != r:
            h = (l + r) // 2
            if nums[h] == target:
                return h
            elif target > nums[h]:
                l = h
            elif target < nums[h]:
                r = h

        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1


sol = Solution()
print(sol.search([3,5,1],4))