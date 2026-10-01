class Solution:
    def make_permute(self, curr_permute, nums, lookup, n, all_permutes ):
        if lookup == [1]*n :
            all_permutes.append(curr_permute[:])
            return
        for i in range(n):
            if lookup[i] == 0 :
                lookup[i] = 1
                curr_permute.append(nums[i])
                self.make_permute( curr_permute, nums, lookup, n, all_permutes )
                lookup[i] = 0
                curr_permute.pop()
        return

    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        all_permutes = []
        lookup = [0] * n
        self.make_permute( [], nums, lookup, n, all_permutes )
        return all_permutes