

A = [3,1,2,4]

class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        A.sort(key=lambda x: x % 2)

A


[x for x in A if x % 2 == 0] + [y for y in A if y % 2 == 1]


