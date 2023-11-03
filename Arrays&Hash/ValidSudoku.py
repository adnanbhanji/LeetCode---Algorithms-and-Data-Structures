class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        final_boxindex = {}

        # rows
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    pass
                elif int(board[i][j]) in range(1,10):
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
                else:
                    return False
            seen = set()

        # cols
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] == ".":
                    pass
                elif int(board[j][i]):
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
                else:
                    return False
            seen = set()

        # boxes
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    pass
                elif int(board[i][j]):
                    if (i//3, j//3) in final_boxindex.keys():
                        if board[i][j] in final_boxindex[(i//3, j//3)]:
                            return False
                        final_boxindex[(i//3, j//3)].add(board[i][j])
                    else:
                        final_boxindex[(i//3, j//3)] = set()
                        final_boxindex[(i//3, j//3)].add(board[i][j])
                else:
                    return False

        return True 
