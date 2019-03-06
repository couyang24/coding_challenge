area = 8

mid = int((area+1)/2)
for num1 in range(mid):
    for num2 in range(mid):
        if (mid - num1)*(mid - num2) == area:
            print([mid - num1, mid - num2])
            break

round(area/2)
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = area
        for num1 in range(mid):
            for num2 in range(mid):
                if (mid + num1) * (mid - num2) == area:
                    return [mid + num1, mid - num2]
        return [area, 1]
