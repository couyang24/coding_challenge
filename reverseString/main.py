s = ["h","e","l","l","o"]

s[::-1]

s.reverse()
s

news = []
for letter in s[::-1]:
    news.append(letter)
print(news)







class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        news=[]
        for letter in s[::-1]:
            news.append(letter)
        return news

