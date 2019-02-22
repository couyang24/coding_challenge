A = [[1,1,0],[1,0,1],[0,0,0]]
x = [1,1,0]

x[::-1]

ans=[]
for row in A:
    ans.append([x^1 for x in row[::-1]])
print(ans)



class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        ans = []
        for row in A:
            newrow = []
            for num in row[::-1]:
                if num == 0:
                    newrow.append(1)
                else:
                    newrow.append(0)
            ans.append(newrow)
        return ans



