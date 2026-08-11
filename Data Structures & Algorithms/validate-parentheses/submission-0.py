class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', '}':'{', ']':'['}
        open_bracket = []
        for c in s:
            if c in dic:#closed
                if open_bracket and dic[c] == open_bracket[-1]:
                    open_bracket.pop()
                else:
                    return False
            else:#open
                open_bracket.append(c)
        return True if not open_bracket else False