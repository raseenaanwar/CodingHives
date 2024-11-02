numbers=[1,2,2,4,4]
unique=set(numbers)
print(unique)
#new_set={expresion for item in iterable if condition}
#squares of numbers from 1 to 5 only for numbers greater than 2
square={x**2 for x in range(1,6) if x>2}
print(square)
#unique letters in a word
word="programming"
unique_letters={letter for letter in word}
print(unique_letters)
#filter even nos
numbers=[1,2,2,3,4,5,6,6,7,8,8]
even={num for num in numbers if num%2==0}
print(even)
#practical application
emails=["asha@examples.com","bob@yahoo.com","mini@examples.com","dinil@sample.net"]
domains={email.split('@')[1] for email in emails}
print(domains)
#uniques hashtags
post="this is #coding tutorial in #python for #beginners and #coders"
uniques_tags={word for word in post.split() if word.startswith('#')}
print(uniques_tags)