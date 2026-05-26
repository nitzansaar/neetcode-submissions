class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate each row
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen or int(val) > 9 or int(val) < 1:
                    return False
                seen.add(val)
        
        # validate each column
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen or int(val) > 9 or int(val) < 1:
                    return False
                seen.add(val)
        
        # validate each sub box
        for row_boundary in range(0, 9, 3):
            for column_boundary in range(0, 9, 3):
                seen = set()
                for r in range(row_boundary, row_boundary + 3):
                    for c in range(column_boundary, column_boundary + 3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in seen or int(val) > 9 or int(val) < 1:
                            return False
                        seen.add(val)
        return True

                
                    

