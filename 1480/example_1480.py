def running_sum(numbers):
    accumulator = 0
    result = []
    for number in numbers:
        accumulator += number
        result.append(accumulator)
    return result


def runningSum_2(self, nums):
    result = []
    if len(nums) > 0:
        result.append(nums[0])
        for index in range(1, len(nums)):
            result.append(nums[index] + result[index - 1])
    return result

