class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) <= 1:
            return 0
        A.sort()
        ans = 0
        for i in range(1 , len(A)):
            if A[i] <= A[i-1]:
                temp = A[i]
                A[i] = A[i-1] + 1
                ans += A[i]-temp
        return ans
        