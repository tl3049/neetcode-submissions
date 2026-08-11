class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in range(n - 1, -1, -1):
            if s[i] not in dic:
                stack.append(s[i])
            else:
                if stack and dic[s[i]] == stack.pop():
                    continue
                else:
                    return False
        return not stack

        
        
        # for i in range(n//2):
        #     if s[i] in dic and dic[s[i]] == s[n - 1 - i]:
        #         continue
        #     else:
        #         return False
        # return True
            
