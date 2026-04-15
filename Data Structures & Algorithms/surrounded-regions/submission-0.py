class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """ 
        Iterate over the board 
        when you encounter a o check to the right 
        check to the bottom check diagonally
        """

        directions = [
            (1,0),
            (0,1), 
            (1,1)
        ]
        def check(r, c): 
            checker = True
            for dx, dy in directions: 
                h = r + dx 
                v = c + dy 
                print(f"Checking this value {h},{v}")
                if 0 <= h < len(board) and 0 <= v < len(board[0]):
                    if board[h][v] != 'O': 
                        checker = False 
                        break 
                else:
                    checker = False 
            return checker

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                if board[r][c] == 'O': 
                    if check(r,c): 
                        board[r][c] = "X"
                        board[r + 1][c] = "X"
                        board[r][c + 1] = "X"
                        board[r + 1][c + 1] = "X"
        
                
