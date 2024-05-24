class Solution(object):
    def halveArray(self, nums):

        def insert_in_order(list, value):
            if len(list) == 1:
                if value >= list[0]:
                    return list + [value]
                else:
                    return [value] + list

            i = 0
            j = len(list)-1
            while i < j:
                h = (j+i) // 2
                if i+1 == j:
                    if value >= list[j]:
                        return list + [value]
                    elif value <= list[i]:
                        return [value] + list
                    else:
                        return list[0:i+1] + [value] + list[j:]
                elif list[h] < value:
                    i = h
                elif list[h] > value:
                    j = h
                else:
                    return list[:h] + [value] + list[h:]
        nums.sort()
        total = 0
        for number in nums:
            total += number
        half = total / 2
        operations = 0
        temp = total
        while temp >= half:
            temp_sus = (nums[-1]/2)
            temp = temp - temp_sus
            nums = insert_in_order(nums[:-1], temp_sus)
            operations += 1
        return operations


sol = Solution()
print(sol.halveArray([5,19,8,1]))
print(sol.halveArray([3,8,20]))
print(sol.halveArray([58,23]))
print(sol.halveArray([18,22,62,61,1,88,17,98,38,32,51,57,7,29,40,61,62,13,89,41,73,85,88,60,59,76,71,76,76,41,29,43,19,9,79]))