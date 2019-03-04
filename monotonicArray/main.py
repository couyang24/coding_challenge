A = [1,2,2,3]


if sorted(A) == A:
    print(True)
elif sorted(A, reverse=True) == A:
    print(True)
else:
    print(False)

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if sorted(A) == A:
            return True
        elif sorted(A, reverse=True) == A:
            return True
        else:
            return False







up = down = True

for index in range(len(A)-1):
    if A[index+1] > A[index]:
        down = False
    if A[index+1] < A[index]:
        up = False
print(up or down)



class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        up = down = True
        for index in range(len(A)-1):
            if A[index+1] > A[index]:
                down = False
            if A[index+1] < A[index]:
                up = False
        return up or down
