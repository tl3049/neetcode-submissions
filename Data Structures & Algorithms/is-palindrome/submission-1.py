class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaCharacter(s[l]):
                l += 1
            while l < r and not self.alphaCharacter(s[r]):
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True


    def alphaCharacter(self, c):
        if ord("A") <= ord(c) <= ord("Z"):
            return ord(c) - ord("A") + ord("a")
        elif ord("a") <= ord(c) <= ord("z"):
            return ord(c)
        elif ord("0") <= ord(c) <= ord("9"):
            return ord(c)
        else:
            return False