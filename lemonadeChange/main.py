bills = [5,5,5,10,20]
bills = [5,5,10]
bills = [10,10]
bills = [5,5,10,10,20]




check = True
wallet = {5:0, 10:0, 20:0}
for bill in bills:
    if bill == 5:
        wallet[bill] += 1
    elif bill == 10:
        if wallet[5] > 0:
            wallet[5] -= 1
            wallet[bill] += 1
        else:
            check = False
    else:
        if wallet[10]>0 and wallet[5]>0:
            wallet[5] -= 1
            wallet[10] -= 1
            wallet[bill] += 1
        elif wallet[5]>2:
            wallet[5] -= 3
            wallet[bill] += 1
        else:
            check = False
print(check)

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        check = True
        wallet = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                wallet[bill] += 1
            elif bill == 10:
                if wallet[5] > 0:
                    wallet[5] -= 1
                    wallet[bill] += 1
                else:
                    check = False
            else:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[5] -= 1
                    wallet[10] -= 1
                    wallet[bill] += 1
                elif wallet[5] > 2:
                    wallet[5] -= 3
                    wallet[bill] += 1
                else:
                    check = False
        return check