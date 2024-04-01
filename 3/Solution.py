class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        current_substring = ""
        start = 0
        index = 0

        size_of_string = len(s)

        while index < size_of_string and start < size_of_string:
            if current_substring.find(s[index]) == -1:
                current_substring += s[index]
                index += 1
            else:
                max_length = max(max_length, len(current_substring))
                current_substring = ""
                start += 1
                index = start


        return max(max_length, len(current_substring))

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring("dvdf"))
print(solution.lengthOfLongestSubstring(" "))