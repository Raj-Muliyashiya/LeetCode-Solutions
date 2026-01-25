class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for raw in range(9):
            new_set = set()
            for coll in range(9):
                if board[raw][coll] == ".":
                    pass
                elif board[raw][coll] in new_set:
                    return False
                else:
                    new_set.add(board[raw][coll])


        for coll in range(9):
            new_set = set()
            for raw in range(9):
                if board[raw][coll] == ".":
                    pass
                elif board[raw][coll] in new_set:
                    return False
                else:
                    new_set.add(board[raw][coll])

        for i in range(0,9,3):
            for j in range(0,9,3):
                metrix = set()
                for st in range(3):
                    for end in range(3):
                        a = board[i+st][j+end]
                        if a == ".":
                            pass
                        elif a in metrix:
                            return False
                        else:
                            metrix.add(a)
        
        return True
        