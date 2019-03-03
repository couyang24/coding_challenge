nums = [[1, 2],
        [3, 4],
        [5, 6]]
r = 2
c = 3

nums = [[1,2],
        [3,4]]
r = 2
c = 4

nums = [[1,2],
 [3,4]]
r = 1
c = 4

nums = [[1, 2],
        [3, 4],
        [5, 6],
        [7, 8]]
r = 4
c = 2


len(nums)
len(nums[0])

if len(nums)*len(nums[0]) != r*c:
    print(nums)
else:
    raw = []
    ans = [[0 for col in range(c)] for row in range(r)]
    for i in nums:
        for j in i:
            raw.append(j)
    for i, m in enumerate(ans):
        for j, n in enumerate(m):
            print(str(i)+str(j))
            ans[i][j] = raw[i*len(ans[0])+j]
    print(ans)





class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
            break
        raw = []
        ans = [[0 for col in range(c)] for row in range(r)]
        for i in nums:
            for j in i:
                raw.append(j)
        for i, m in enumerate(ans):
            for j, n in enumerate(m):
                print(str(i) + str(j))
                ans[i][j] = raw[i * len(ans[0]) + j]
        return ans
