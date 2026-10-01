class Solution:
    def valid( self, row, col, n, arrangement ):
        tempr = row
        tempc = col
        while tempr >=0  :
            if arrangement[tempr][tempc] == "Q" : return False
            tempr -= 1
        tempr = row
        tempc = col
        while tempr >= 0 and tempc >= 0 :
            if arrangement[tempr][tempc] == "Q" : return False
            tempr -= 1
            tempc -= 1
        tempr = row
        tempc = col
        while tempr >= 0 and tempc < n:
            if arrangement[tempr][tempc] == "Q" : return False
            tempr -= 1
            tempc += 1
        return True

    def make_arrangement( self, row, all_arrangements, arrangement, n ):
        if row == n:
            all_arrangements.append(["".join(row) for row in arrangement])
            return
        for col in range(n):
            if self.valid( row, col, n, arrangement ) :
                arrangement[row][col] = "Q"
                self.make_arrangement( row+1, all_arrangements, arrangement, n )
                arrangement[row][col] = "."
        return
            
    def solveNQueens(self, n: int) -> list[list[str]]:
        all_arrangements = []
        arrangement = [["."] * n for _ in range(n)]
        self.make_arrangement( 0, all_arrangements, arrangement, n )
        return all_arrangements