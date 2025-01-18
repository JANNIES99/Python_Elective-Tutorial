words=input("Enter the word to be encoded:")
key=int(input("Enter the code to be encoded:"))
smallCase=words.lower()
encodedWords=""
for i in smallCase:
    asciiValue=ord(i)
    if(asciiValue>=ord("a")and asciiValue<=ord("z")):
        asciiValue+=key
        if(asciiValue>ord("z")):
            asciiValue=asciiValue-ord("z")
            asciiValue=asciiValue+ord("a")-1
    encodedWords=encodedWords+chr(asciiValue)

casedEncodedWord=""
for i in range(len(words)):
    if words[i].isupper():
        casedEncodedWord=casedEncodedWord+encodedWords[i].upper()
    else:
        casedEncodedWord=casedEncodedWord+encodedWords[i]

print(casedEncodedWord)