class Solution:
    def isValid(self, s: str) -> bool:
        opening_parens = ['(', '{', '[']
        closing_parens = [')', '}', ']']
        open_parens_stack = []
        list_of_paren = list(s)

        for paren in list_of_paren:
            if paren in opening_parens:
                open_parens_stack.append(paren)
            else:
                if len(open_parens_stack) == 0:
                    return False
                open_paren = open_parens_stack.pop()
                open_paren_index = opening_parens.index(open_paren)
                closing_parens_index = closing_parens.index(paren)
                if open_paren_index != closing_parens_index:
                    return False
        return len(open_parens_stack) == 0


sol = Solution()

print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))

