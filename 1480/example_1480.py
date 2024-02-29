def running_sum(numbers):
    accumulator = 0
    result = []
    for number in numbers:
        accumulator += number
        result.append(accumulator)
    return result

