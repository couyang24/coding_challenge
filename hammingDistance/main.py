x = 1
y = 4

y/2


class Solution:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        result = 0

        while x != 0 or y != 0:
            xRemin = x % 2
            yRemin = y % 2
            if xRemin == yRemin:
                result += 1
            x = x//2
            y = y//2
        print(result)


