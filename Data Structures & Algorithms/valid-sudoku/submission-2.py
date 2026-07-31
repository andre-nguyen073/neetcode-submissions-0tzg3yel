class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ 
        Create three seperate sets: Row, Boxes, Columns 
        Iterate over each row/column, check if repeated values in any 
        Then you can return False
        Else Return True

        Why do you need area of the board: 
        """
        r_mp = defaultdict(set)
        c_mp = defaultdict(set)
        box_mp = defaultdict(set)

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                #make sure number is between 1-9
                if board[r][c] == '.': 
                    continue
                curr = int(board[r][c])
                if curr >= 1 or curr <= 9: 
                    #get the area of the board 
                    #box values - gonna get 0 - 2 
                    row = r // 3 
                    col = c // 3
                    if curr in box_mp[(row,col)]: 
                        return False 
                    else: 
                        box_mp[(row,col)].add(curr)

                    if curr in r_mp[r]: 
                        return False 
                    else: 
                        r_mp[r].add(curr)
                    
                    if curr in c_mp[c]: 
                        return False 
                    else: 
                        c_mp[c].add(curr)
                else: 
                    return False
        return True

        