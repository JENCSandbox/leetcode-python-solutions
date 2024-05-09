class Solution(object):
    def int_to_inverted_list(self, x):
        # -2 147 483 647 to 2 147 483 647
        list_result = []
        temp = x
        while temp > 0:
            list_result.append(temp % 10)
            temp //= 10

        while len(list_result) < 10:
            list_result.insert(0, 0)

        return list_result

    def is_valid_max_possible_number(self, number_list, sign):
        max_number = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8] if sign else [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]
        index_to_verify = 0
        result = False
        while index_to_verify < 10:

            print("verifying")

            i_eth_number = number_list[index_to_verify]
            i_eth_max = max_number[index_to_verify]

            if i_eth_number > i_eth_max:
                result = False
                break

            elif i_eth_number < i_eth_max:
                result = True
                break

            else:
                index_to_verify += 1

        return result

    def list_to_number(self, list):
        result = 0
        index = 0

        while index < len(list):
            digit = list[index]
            result = 10*result + digit
            index +=1
        return result

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_inverted_list = self.int_to_inverted_list(abs(x))
        print('Reversed List')
        print(x_inverted_list)

        sign = True if x < 0 else False
        valid = self.is_valid_max_possible_number(x_inverted_list, sign)
        sign_applied = -1 if sign else 1
        return sign_applied * self.list_to_number(x_inverted_list) if valid else 0

