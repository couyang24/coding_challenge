nums = [2, 7, 11, 15]
target = 9

for inputIndex1 in range(len(nums)):
    for inputIndex2 in range(len(nums)-(inputIndex1+1)):
        if nums[inputIndex1]+nums[inputIndex2+inputIndex1+1] == target:
            print([inputIndex1, inputIndex2+inputIndex1+1])

