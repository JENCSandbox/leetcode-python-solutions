from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        temp = []

        numbers = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        digits_as_list = list(digits)
        for digit_item in digits_as_list:
            numbers_by_digit = numbers.get(digit_item)
            temp.append(numbers_by_digit)


        for letters_group in temp:
            if len(result) == 0:
                result = letters_group
            else:
                temp_combinations = []
                for combination in result:
                    for letter in letters_group:
                        temp_combinations.append(combination+letter)
                result = temp_combinations

        return result




sol = Solution()
print(sol.letterCombinations("234"))