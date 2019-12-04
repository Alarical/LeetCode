class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.') + [0]*4
        v2 = version2.split('.') + [0]*4
        for i in range(4):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            else:
                continue
        return 0
