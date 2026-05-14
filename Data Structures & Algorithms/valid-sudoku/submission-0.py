class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        colums = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        output = True
        for i in range(9):
            for j in range(9):
                num = board[i][j] 
                if num != ".":                
                    if num in rows[i]:
                        output=False
                        break
                    if num in colums[j]:
                        output=False
                        break
                    if num in boxes[(i//3)*3 + (j//3)]:
                        output=False
                        break
                    rows[i].add(num)
                    colums[j].add(num)
                    boxes[(i//3)*3 + (j//3)].add(num)
        return output
