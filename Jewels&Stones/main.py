J = "aA"
S = "aAAbbbb"



class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str'):
        count = 0
        for eachS in S:
            for eachJ in J:
                if eachS == eachJ:
                    count += 1
        return count


numJewelsInStones(J, S)