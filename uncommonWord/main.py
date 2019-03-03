A = "apple apple"
B = "banana"

len(A)
len(B)

A.split()

length = min(len(A), len(B))
ans = []
for index in range(length):
    if A[index] == ' ':
        checkpoint = index+1
    if A[index] != B[index]:
        diff = index
        break

ans.append(A[checkpoint:])
ans.append(B[checkpoint:])
print(ans)

A = "this apple is sweet"
B = "this apple is sour"
A = "apple apple"
B = "banana"

count = {}
for word in A.split():
    count[word] = count.get(word, 0) + 1
for word in B.split():
    count[word] = count.get(word, 0) + 1
[word for word in count if count[word] == 1]

A = "this apple is sweet"
B = "this apple is sour"

ans = []
count = {}
for word in A.split():
    if word in count.keys():
        count[word] += 1
    else:
        count[word] = 1

for word in B.split():
    if word in count.keys():
        count[word] += 1
    else:
        count[word] = 1
for word in count:
    if count[word] == 1:
        ans.append(word)

print(ans)


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:

        ans = []
        count = {}
        for word in A.split():
            if word in count.keys():
                count[word] += 1
            else:
                count[word] = 1

        for word in B.split():
            if word in count.keys():
                count[word] += 1
            else:
                count[word] = 1
        for word in count:
            if count[word] == 1:
                ans.append(word)
        return ans