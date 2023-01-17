class Solution(object):
    def has_repetition(self, lst):
        for x in lst:
            if x != '.':
                if lst.count(x) > 1:
                    return True
        return False

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        length = len(board)
        
        # row check
        for row in range(0, length):
            if self.has_repetition(board[row]):
                return False
        
        # col check
        for row in range(0, length):
            col = [board[i][row] for i in range(0, length)]
            if self.has_repetition(col):
                return False
        
        # for each 3x3 box
        for row in range(0, length, 3):
            for col in range(0, length, 3):
                box = []
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        box.append(board[i][j])
                print("box: ", box)
                if self.has_repetition(box):
                    return False
        
        return True

board = [[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]

sl = Solution()
print(sl.isValidSudoku(board))