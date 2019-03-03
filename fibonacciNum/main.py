N = 2





fst = 0
sec = 1

if N  == 0:
    print(0)
elif N == 1:
    print(1)
else:
    result = 0
    for x in range(1, N):
        result = sec + fst
        fst = sec
        sec = result













class Solution:
    def fib(self, N: int) -> int:
        if N  == 0:
            return 0
        elif N == 1:
            return 1
        else:
            result = 0
            for x in range(1, N):
                result = sec + fst
                fst = sec
                sec = result
            return result