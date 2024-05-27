from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}  # "word, list"

        for word in strs:
            sorted_word = str(sorted(word))
            if dic.get(sorted_word) is not None:
                dic[sorted_word] = dic[sorted_word] + [word]
            else:
                dic[sorted_word] = [word]

        return list(dic.values())