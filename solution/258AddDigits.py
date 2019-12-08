class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        for i in str(num):
            ans += int(i)
        while ans >= 10:
            temp = 0
            for i in str(ans):
                temp += int(i)
            ans = temp
        return ans
    #根据对9取余的结果返回
    #return (num - 1) % 9 + 1