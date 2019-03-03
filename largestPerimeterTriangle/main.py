A = [3,6,2,3]
A = [3,2,3,4]
A = [1,2,1]



A.sort(reverse=True)
for index in range(len(A)-2):
    if A[index] < A[index+1]+A[index+2]:
        print(A[index]+A[index+1]+A[index+2])
        break
    if index == len(A)-3:
        print(0)







class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for index in range(len(A)-2):
            if A[index] < A[index+1]+A[index+2]:
                return A[index]+A[index+1]+A[index+2]
                break
            if index == len(A)-2:
                return 0