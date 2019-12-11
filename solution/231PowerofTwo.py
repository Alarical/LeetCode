class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # while n > 1:
        #     n = n/2
        # if n == 1:
        #     return True
        # else:
        #     return False
        return n > 0 and (n & (n-1)) == 0