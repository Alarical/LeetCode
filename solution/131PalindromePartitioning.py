class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            i = 0
            j = len(s)-1
            while i<=j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True

        def dfs(s , i , temp, res ):
            if i == len(s):
                res.append(temp.copy())
                return
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    temp.append(s[i:j+1])
                    dfs(s , i+1 , temp , res )
                    temp.pop()

        res = []
        temp = []
        dfs(s, 0 , temp , res)
        return res
