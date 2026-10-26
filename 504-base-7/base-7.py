class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0 : return "0"
        temp = num if num > 0 else -num
        result = ''
        while temp != 0 :
            result = str(temp % 7) + result
            temp //= 7
        if num < 0 :
            result = "-" + result
        return result