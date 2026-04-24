class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = defaultdict(set)
        vertical = defaultdict(set)
        sub_box = defaultdict(set)

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                sub_r = r // 3 
                sub_c = c // 3
                if board[r][c] in horizontal[r]: 
                    return False 
                elif board[r][c] in vertical[c]: 
                    return False
                elif board[r][c] in sub_box[(sub_r, sub_c)]:
                    return False
                if board[r][c] != '.':
                    horizontal[r].add(board[r][c])
                    vertical[c].add(board[r][c])
                    sub_box[(sub_r, sub_c)].add(board[r][c])
        
        return True