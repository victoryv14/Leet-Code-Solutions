class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        result = [-1,-1]
        i = 1
        while i * i <= area:
            if area % i == 0:
                result[0] = area // i
                result[1] = i
            i += 1
        return result