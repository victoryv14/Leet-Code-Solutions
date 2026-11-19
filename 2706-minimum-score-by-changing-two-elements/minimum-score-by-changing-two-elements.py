class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        opt1 = nums[n - 3] - nums[0]
        opt2 = nums[n - 1] - nums[2]
        opt3 = nums[n - 2] - nums[1]

        return min(opt1, opt2, opt3)