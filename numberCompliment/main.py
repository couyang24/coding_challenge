num = 5

num % 2
5//2

count = 0

while num != 0:
    if num % 2 == 1:
        count += 1
    num = num // 2

print(count)






class Solution:
    def findComplement(self, num: int) -> int:
        count = 0

        while num // 2 != 0:
            if num % 2 == 1:
                count += 1
            num = num / 2

        return count