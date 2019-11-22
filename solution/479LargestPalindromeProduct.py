#超时
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        Max = 10**n -1 # n = 2 max = 99
        for i in range(Max-1 , Max//10 , -1):
            num = int(str(i) + str(i)[::-1])
            j = Max
            while j*j >= num:
                if num % j == 0:
                    return num % 1337
                j -= 1
        return -1
