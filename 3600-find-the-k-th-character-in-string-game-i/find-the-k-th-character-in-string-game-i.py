class Solution:
    def kthCharacter(self, k: int) -> str:
        size = 1
        result = 'a'
        while size < k:
            for i in range(size):
                result += chr(ord(result[i]) + 1)
            size *= 2
        return result[k-1]