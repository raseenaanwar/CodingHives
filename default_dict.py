#defaultdict
# freq={}
# for letter in word:
#     if letter in freq:
#         freq[letter]+=1
#     else:
#         freq[letter]=1
# print(freq)
from collections import defaultdict
word="python"
freq=defaultdict(int)
for letter in word:
    freq[letter]+=1
print(freq)

