from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = [] # (dic, array_of_words)
        result_final = []
        def to_dic_count(word):
            result_dic = {}

            for letter in word:
                if result_dic.get(letter) is not None:
                    result_dic[letter] += 1
                else:
                    result_dic[letter] = 0
            return result_dic

        for word in strs:
            word_dic = to_dic_count(word)
            inserted = False
            for index, item in enumerate(result):
                (dic, array_of_words) = item
                if word_dic == dic:
                    result[index] = (dic, array_of_words+[word])
                    inserted = True
                    break
            if not inserted:
                result += [(word_dic, [word])]


        for item in result:
            result_final += [item[1]]
        return result_final