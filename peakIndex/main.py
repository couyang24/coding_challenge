A = [0, 1, 0]
A = [0,2,1,0]

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1, len(A)-1):
            if A[i] > A[i+1] and A[i] > A[i-1]:
                return i