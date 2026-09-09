N = 1000001
spf = [0] * N
for i in range(N): spf[i] = i
i = 2
while i * i < N:
    if spf[i] == i :
        j = i * i
        while j < N:
            if spf[j] == j : spf[j] = i
            j += i
    i += 1

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(-2,-(len(nums)+1),-1):
            if( nums[i] > nums[i+1] ) :
                nums[i] = spf[nums[i]]
                operations += 1
                if( nums[i] > nums[i+1] ) : return -1
        return operations