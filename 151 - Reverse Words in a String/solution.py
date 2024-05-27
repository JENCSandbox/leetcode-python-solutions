import collections


class Solution:
    def reverseWords(self, s: str) -> str:
        deque = collections.deque()
        temp_word = ""

        for letter in s:
            if letter == " ":
                if temp_word != "":
                    deque.append(temp_word)
                    temp_word = ""
            else:
                temp_word += letter

        if len(temp_word) > 0:
            deque.append(temp_word)

        result = ""
        print(deque)
        while len(deque) > 1:
            word = deque.pop()
            if word != "":
                result += word
                result += " "

        return result + deque.pop()

