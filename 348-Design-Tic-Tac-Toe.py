class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

        

    def move(self, row: int, col: int, player: int) -> int:
        curr_player = 1 if player == 1 else -1
        self.row[row] += curr_player
        self.col[col] += curr_player
        if row == col:
            self.diag += curr_player
        if col + row == self.n - 1:
            self.anti_diag += curr_player
        
        # print(row, col, curr_player, self.row, self.col, self.diag, self.anti_diag)
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)