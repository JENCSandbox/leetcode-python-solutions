# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome_string = ""
        max_palindrome_string_length = 0
        size_of_string = len(s)
        for i in range(size_of_string):
            l, r_odd = i, i

            while l >= 0 and r_odd < size_of_string and s[l] == s[r_odd]:
                if (r_odd - l + 1) > max_palindrome_string_length:
                    max_palindrome_string = s[l:r_odd + 1]
                    max_palindrome_string_length = len(max_palindrome_string)
                l -= 1
                r_odd += 1

            l, r_even = i, i + 1
            while l >= 0 and r_even < size_of_string and s[l] == s[r_even]:
                if (r_even - l + 1) > max_palindrome_string_length:
                    max_palindrome_string = s[l:r_even + 1]
                    max_palindrome_string_length = len(max_palindrome_string)
                l -= 1
                r_even += 1
        return max_palindrome_string
