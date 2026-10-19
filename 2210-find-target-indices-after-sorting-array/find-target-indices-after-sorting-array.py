class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        target_indices = []
        for i in range(len(nums)):
            if nums[i] == target : target_indices.append(i)
            elif nums[i] > target : break
        return target_indices