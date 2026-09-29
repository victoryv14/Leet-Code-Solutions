class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        def get_maxdiff(i, j):
            if i == j:
                return nums[i]
            take_left = nums[i] - get_maxdiff(i + 1, j)
            take_right = nums[j] - get_maxdiff(i, j - 1)
            return max(take_left, take_right)
        return get_maxdiff(0,len(nums)-1) >= 0
