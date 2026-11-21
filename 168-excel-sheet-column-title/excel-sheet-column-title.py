class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber > 0 and columnNumber <= 26 :
            return chr(columnNumber + 64)
        if columnNumber % 26 != 0 :
            char = chr( (columnNumber % 26) + 64 )
            return self.convertToTitle(columnNumber//26) + char
        else :
            char = "Z"
            return self.convertToTitle(columnNumber//26 - 1) + char