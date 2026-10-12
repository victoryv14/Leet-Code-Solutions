class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        bulbs_states = [0]*101
        for i in bulbs :
            bulbs_states[i] ^= 1 
        result = []
        for i in range(1,101):
            if bulbs_states[i] : result.append(i)
        return result