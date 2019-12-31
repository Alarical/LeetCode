class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for c1,c2 in zip(s,t):

            if c1 in dic and c2 != dic[c1]:
                return False

            if c1 not in dic and c2 in dic.values():
                return False

            dic[c1] = c2

        return True
