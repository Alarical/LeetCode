class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        ans = ['']
        phone = ['', 'abc' , 'def' , 'ghi' ,'jkl' , 'mno' ,'pqrs' ,'tuv' ,'wxyz']
        for num in digits:
            temp = []
            charsets = phone[int(num)-1]
            for already in ans:
                for char in charsets:
                    temp.append(already+char)
            ans = temp
        return ans