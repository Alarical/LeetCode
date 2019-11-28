# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = (rand7()-1) * 7 + rand7() # 0-42 + 1-7 = 1-49
            if a <= 40:
                return a%10+1
        return 0
