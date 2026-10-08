class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indexes = {}
        for i in range(len(nums)):
            if nums[i] not in indexes :
                indexes[nums[i]] = [i]
            else :
                indexes[nums[i]].append(i)
        for positions in indexes.values():
            for i in range(1,len(positions)):
                if positions[i] - positions[i-1] <= k :
                    return True
        return False