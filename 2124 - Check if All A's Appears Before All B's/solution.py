class Solution:
    def checkString(self, s: str) -> bool:
        a_lasted_index = -1
        b_lasted_index = -1

        for i, letter in enumerate(s):
            if letter == 'a' and b_lasted_index != -1 and i > b_lasted_index:
                return False
            elif letter == 'a' and b_lasted_index == -1:
                a_lasted_index = i

            elif letter == 'b' and (a_lasted_index == -1 or b_lasted_index == -1):
                b_lasted_index = i

            elif letter == 'b' and a_lasted_index != -1:
                if a_lasted_index > b_lasted_index:
                    return False
                else:
                    b_lasted_index = i

        return True


