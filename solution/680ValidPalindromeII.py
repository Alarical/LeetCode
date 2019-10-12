class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            n = len(s)
            i = 0
            j = n-1
            while i < j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                break
        if i >= j:
            return True
        else:
            return isPalindrome(s[:i] + s[i+1:]) or isPalindrome(s[:j]+s[j+1:])


