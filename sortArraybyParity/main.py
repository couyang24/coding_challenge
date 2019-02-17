

A = [3,1,2,4]

class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        A.sort(key=lambda x: x % 2)

A


