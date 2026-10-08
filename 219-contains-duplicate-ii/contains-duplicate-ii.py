class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indexes = {}
        for i in range(len(nums)):
            if nums[i] not in indexes :
                indexes[nums[i]] = i
            else :
                temp = i - indexes[nums[i]]
                if temp <= k :
                    return True
                indexes[nums[i]] = i
        return False