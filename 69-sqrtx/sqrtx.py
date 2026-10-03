class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1 : return x
        i = 2 
        while i * i <= x :
            if( i * i == x ) : return i
            i += 1
        return i - 1