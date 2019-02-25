points = [[1,3],[-2,2]]
K = 1

points.sort(key = lambda x: x[0]**2 + x[1]**2)
points[:K]

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:K]