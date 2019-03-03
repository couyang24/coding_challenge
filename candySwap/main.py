A = [1,2,5]
B = [2,4]

A = [1,1]
B = [2,2]

A = [1, 2]
B = [2, 3]

A = [2]
B = [1,3]

check = False
for itemA in A:
    for itemB in B:
        if sum(A)-itemA+itemB == sum(B)-itemB+itemA and check == False:
            check = True
            print([itemA, itemB])

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        check = False
        for itemA in A:
            for itemB in B:
                if sum(A) - itemA + itemB == sum(B) - itemB + itemA and check == False:
                    check = True
                    return [itemA, itemB]




for item in A:
    if item+(sum(B)-sum(A))/2 in set(B):
        itemB =item+(sum(B)-sum(A))/2
        print([item, int(itemB)])

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        for item in A:
            if item + (sum(B) - sum(A)) / 2 in set(B):
                itemB = item + (sum(B) - sum(A)) / 2
                return [item, int(itemB)]