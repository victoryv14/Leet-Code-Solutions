class Solution(object):
    def do_digit_sum( self, n ):
        digit_sum = 0
        while(n > 0):
            digit_sum += n % 10
            n //= 10
        return digit_sum
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            if self.do_digit_sum(nums[i]) == i :
                return i
        return -1