from breezypythongui import EasyFrame
import random
class guessingGame (EasyFrame):
    num=random.randint(1,100)
    attempts=1
    def __init__(self):
        EasyFrame.__init__(self,title="Guessing Game")
        self.outputLabel=self.addLabel(text="Guess a number from 1 to 100",row=0,column=0,columnspan=2)
        #self.addLabel(text="Guess a number from 1 to 100",row=0,column=0,columnspan=2)
        self.addLabel(text="Your Guess",row=1,column=0)
        self.inputField=self.addTextField(text="",row=1,column=1)
        #self.outputLabel=self.addLabel(text="",row=2,column=0)
        self.addButton(text="Next",row=2,column=0,command=self.guessValue)
        self.addButton(text="New Game",row=2,column=1,command=self.newGame)
    def guessValue(self):
        text=self.inputField.getText()
        num2=int(text)
        if(self.num==num2):
            self.outputLabel["text"]="Your guessed the right number in "+str(self.attempts)+" attempts!"
        elif(self.num>num2):
            self.outputLabel["text"]="Your guess is too small"
            self.attempts+=1
        else:
            self.outputLabel["text"]="Your guess is too big"
            self.attempts+=1
    def newGame(self):
        self.num=random.randint(1,100)
        self.attempts=1
        self.outputLabel["text"]="Guess a number from 1 to 100"

def main():
    guessingGame().mainloop()

if __name__ == "__main__":
    main()