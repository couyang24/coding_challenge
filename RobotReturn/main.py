moves = "UD"

class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        vert = 0
        hori = 0
        for ins in moves:
            if ins == 'U':
                vert += 1
            elif ins == 'D':
                vert -= 1
            elif ins == 'R':
                hori += 1
            else:
                hori -= 1
        if (vert, hori) == (0, 0):
            print('true')
        else:
            print('false')