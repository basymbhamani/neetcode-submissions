class Solution:
    def containsDuplicate(self, nums: List[str]) -> bool:
        nums_present = set()
        for n in nums:
            if n in nums_present:
                return True
            if n != ".":
                nums_present.add(n)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.containsDuplicate(row):
                return False

        for i in range(9):
            column = [0] * 9
            for j in range(9):
                column[j] = board[j][i]
            if self.containsDuplicate(column):
                return False
            
        for i in range(3):
            for j in range(3):
                square = []
                for k in range(3):
                    square.extend(board[i*3+k][j*3:j*3+3])
                if self.containsDuplicate(square):
                    return False

        return True