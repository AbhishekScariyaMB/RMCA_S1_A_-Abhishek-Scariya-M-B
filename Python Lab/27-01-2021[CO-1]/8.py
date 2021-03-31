word=str(input("Enter a word: "))
x=word[0]
word=word.replace(x,"$")
word=x+word[1:]
print(word)