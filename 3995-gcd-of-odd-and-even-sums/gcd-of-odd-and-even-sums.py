class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a,b):
            while b != 0:
                temp = a % b
                a = b
                b = temp
            return a
        return gcd( n**2 , n*(n+1) )