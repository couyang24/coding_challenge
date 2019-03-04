num = 38




while num >= 10:
    median = 0
    for digit in str(num):
        median += int(digit)
    num = median

print(num)
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            median = 0
            for digit in str(num):
                median += int(digit)
            num = median
        return num



