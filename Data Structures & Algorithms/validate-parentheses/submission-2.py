class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        # print(n)
        dic = {'(':')', '{': '}', '[':']'}
        for i in range(n):
            if s[i] in dic:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    key = stack.pop()
                    if dic[key] != s[i]:
                        return False
        if not stack:
            return True
        else:
            return False
            
            
        #     if i < n//2:
        #         stack.append(s[i])
        #     else:
        #         print(stack[-1])
        #         print(s[i])
        #         key = stack[-1]
        #         if key not in dic:
        #             return False
        #         else:
        #             val = dic[key]
        #         if val == s[i]:
        #             stack.pop()
        #         else:
        #             return False
        # if not stack:
        #     return True
        # else:
        #     return False