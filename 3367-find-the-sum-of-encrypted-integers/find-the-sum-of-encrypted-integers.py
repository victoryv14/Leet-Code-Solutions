class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            s = str(i)
            max_char = max(s)
            encrypted_num = int(max_char * len(s))
            result += encrypted_num
        return result