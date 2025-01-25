f1=open("file.txt","r")
fileText=f1.read()
fileText=fileText.lower()
listOfText=fileText.split()
noOfWord=0
noOfSentence=0
noOfSyllable=0
for i in listOfText:
    if i[0].isalpha():
        noOfWord+=1
        if (len(i)<4):
            noOfSyllable+=1
        else:
            consecutive=0
            for j in i:
                if(j in ["a","e","i","o","u",] and consecutive in [0,1]):
                    consecutive+=1
                elif(consecutive==1):
                    noOfSyllable+=1
                    consecutive=0
                if(consecutive==2):
                    consecutive=0
                    noOfSyllable+=1
            if(i[-1] in [".","?","!",":",";"]):
                if(i[-2:-1] in ["es","ed"] or i[-2]=="e"):
                    noOfSyllable-=1
            else:
                if(i[-2:] in ["es","ed"] or i[-1]=="e"):
                    noOfSyllable-=1
    if i[-1] in [".","?","!",":",";"]:
        noOfSentence+=1


print(noOfWord)
print(noOfSentence)
print(noOfSyllable)
if(noOfSentence)==0:
    noOfSentence=1

F=835.206-1.105*(noOfWord/noOfSentence)-84.6*(noOfSyllable/noOfWord)
G=0.39*(noOfWord/noOfSentence)+11.8*(noOfSyllable/noOfWord)-15.59
print("F=",F)
print("G=",G)

if(G>=0 and G<=30):
    print("College Level")
elif(G<50):
    print("Middle of High School and College Level")
elif(G>=50 and G<=60):
    print("High School Level")
elif(G<90):
    print("Middle of Fourth Grade and High School Level")
elif(G>=90 and G<=100):
    print("Fourth Level")