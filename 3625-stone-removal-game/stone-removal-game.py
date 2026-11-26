class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10 :
            return False
        else:
            i = 0
            stones = 10
            while n - stones >= 0 :
                n -= stones
                stones -= 1
                i += 1
            return True if i % 2 != 0 else False