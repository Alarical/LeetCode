class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dic = {}
        s = str.split(' ')
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dic and s[i] != dic[pattern[i]]:
                print (s[i] , pattern[i])
                return False
            if pattern[i] not in dic and s[i] in dic.values():
                return False
            dic[pattern[i]] = s[i]
        return True