#square numbers 1-10
square=[x**2 for x in range(1,11)]
print(square)
#even numbers 1-20
even=[x for x in range(1,21) if x%2==0]
print(even)
#odd numbers 1-20
odd=[x for x in range(1,21) if x%2==1]
print(odd)
#convert to uppercase
words=["hello",'welcome','to','coding','hives']
upper_words=[word.upper() for word in words]
print(upper_words)
#filter long words >4letters
words=['cat','elephant','dog','giraffe','rat','tiger']
long_words=[word for word in words if len(word)>4]
print(long_words)
#create tuple (1,1)(2,4)...
squared_tuples=[(x,x**2) for x in range(1,6)]
print(squared_tuples)

#create a list of lengths
words=["hello",'welcome','to','coding','hives']
lengths=[len(word) for word in words]
print(lengths)
#Extract digits from a string
s="abc123def456"
digits=[int(char) for char in s if char.isdigit()]
print(digits)
