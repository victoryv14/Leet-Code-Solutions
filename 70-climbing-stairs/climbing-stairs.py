class Solution:
    def climbStairs(self, n: int) -> int:
        temp_1 = 1
        temp_2 = 2
        if n == 1 :
            return temp_1
        elif n == 2 :
            return temp_2
        else :
            for i in range(3,n+1):
                temp = temp_1 + temp_2
                temp_1 = temp_2
                temp_2 = temp
            return temp_2