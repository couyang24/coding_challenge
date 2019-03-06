m = 3
n = 3
operations = [[1,2],[3,3]]

min([op[0] for op in operations])*min(op[1] for op in operations)

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        else:
            return min([op[0] for op in ops])*min(op[1] for op in ops)