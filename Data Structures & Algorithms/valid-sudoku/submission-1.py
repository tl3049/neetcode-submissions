class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(nums, data):
            #print(f'nums:{nums}')
            for i in range(len(nums)):
                if nums[i] == ".":
                    continue
                else: 
                    val = int(nums[i]) - 1
                    data[val] += 1
                    if data[val] > 1:
                        return False
            return True
        for i in range(9):
            data = [0] * 9
            if not check(board[i], data):
                return False
        for i in range(9):
            data = [0] * 9
            res = [board[r][i] for r in range(9)]
            if not check(res, data):
                return False
        for i in range(3):
            for j in range(3):
                data = [0] * 9
                res = [board[r][c] for r in range(i*3, i*3+3) for c in range(j*3, j*3+3)]
                if not check(res[:], data):
                    return False
        return True