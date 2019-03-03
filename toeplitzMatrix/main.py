matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]


ans = {}
for r, row in enumerate(matrix):
  for c, num in enumerate(row):
    if r - c not in ans.keys():
      ans[r-c] = num
    elif ans[r-c] != num:
      print(False)
print(True)


class Solution:
  def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    len(matrix)
    len(row)
    ans = {}
    for r, row in enumerate(matrix):
      for c, num in enumerate(row):
        if r - c not in ans.keys():
          ans[r - c] = num
        elif ans[r - c] != num:
          return False
    return True