class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_str = bin(a).replace('0b','')
        b_str = bin(b).replace('0b','')
        c_str = bin(c).replace('0b','')
        max_len = max( max(len(a_str) , len(b_str)) , len(c_str))
        a_str = a_str.zfill(max_len)
        b_str = b_str.zfill(max_len)
        c_str = c_str.zfill(max_len)
        #('010', '110', '101')
        ans = 0
        for i in range(max_len):
            if int(a_str[i]) + int(b_str[i]) != 2:
                ans += abs((int(a_str[i]) + int(b_str[i])) - int(c_str[i]))
            elif int(c_str[i]) == 1:
                ans += 0
            else:
                ans += 2
        return ans
        #return a_str,b_str,c_str,ans