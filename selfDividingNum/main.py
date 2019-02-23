left = 1
right = 22

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right+1):
            check = True
            for digit in str(num):
                if digit == '0' or num % int(digit) > 0 :
                    check = False
            if check == True:
                ans.append(num)
        return ans