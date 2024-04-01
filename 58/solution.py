class Solution(object):

    def get_last_not_none_item(self, words_array):
        print(words_array)
        reversed_index = -1
        len_of_array = len(words_array)
        last_non_none_word = None
        found = False

        while abs(reversed_index) <= len_of_array and not found:
            last_non_none_word = words_array[reversed_index]
            if last_non_none_word != '':
                found = True
            reversed_index = reversed_index - 1
        return last_non_none_word
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split the string into an array
        words_split_by_space = s.split(' ')

        # get the last item
        last_word = self.get_last_not_none_item(words_split_by_space)
        return len(last_word)


solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
