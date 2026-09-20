class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse_degree = 0
        for i in range(len(s)):
            reverse_degree += (123-ord(s[i]))*(i+1)
        return reverse_degree
