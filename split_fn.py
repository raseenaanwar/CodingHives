#basic split with default separator(spaces)
text="Hello World! Welcome to python"
words=text.split()
print(words)
#split by custom separator(,-)
data="apple,orange,banana,grapes"
fruits=data.split(',')
print(fruits)
#limiting number of splits
sentence="one two three four"
words=sentence.split(" ",2)
print(words)
#remove leading and trailing separators
text=",apple,banana,,"
words=text.split()
print(words)
words=text.strip(",").split(",")
print(words)
#splitting on each character
text="python"
chars=list(text)
print(chars)
#splitlines() to split lines
text="hello coders!\n How are you?\nI am good"
print(text)
lines=text.splitlines()
print(lines)
#split from right side rsplit()
path="folder/subfolder/file.txt"
parts=path.rsplit('/',1)
print(parts)
#combining split() with join()
text="python is fun"
words=text.split()
new_text='-'.join(words)
print(new_text)

text = "one,two,three,four"
print(text.rsplit(",", 1))
