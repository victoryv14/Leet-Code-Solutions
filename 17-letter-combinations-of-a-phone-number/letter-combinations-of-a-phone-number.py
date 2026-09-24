mapp = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz'
}
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n = len(digits)
        result = []
        def recurr( ind, s ):
            if len(s) == n :
                result.append(s)
                return
            for c in mapp[digits[ind]]:
                recurr( ind+1, s+c )
        recurr(0,"")
        return result