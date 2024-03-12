import os
import random

def main():
    gametitle = "Word Raider"
    
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'words.txt')
    
    with open(filename) as f:
        wordbank = f.read().splitlines()
    
    word = random.choice(wordbank).lower()
    
    misplaced = []
    wrong = []
    maxturns = 5
    turns = 0
    
    print(f"Welcome to {gametitle}")
    print("Try to guess the " + str(len(word)) + "-letter word!")
    print("You have " + str(maxturns - turns) + " turns left!" )
    
    success = False
    
    while success == False and turns < maxturns:
        guess = input("What's your guess? ").lower()
        print()
        
        if len(guess) != len(word) or guess.isalpha() == False:
            print("Incorrect input. Please make sure you write a " + str(len(word)) + "-letter word!")
        else:
            for i in range(len(word)):
                if guess[i] == word[i]:
                    print(guess[i], end="")
                    if guess[i] in misplaced:
                        misplaced.remove(guess[i])
                elif guess[i] in word:
                    if guess[i] not in misplaced:
                        misplaced.append(guess[i])
                    print("_", end = "")
                else:
                    if guess[i] not in wrong:
                        wrong.append(guess[i])
                    print("_", end = "")
            
            
            misplaced.sort()
            wrong.sort()
                    
            print()
            print("Misplaced Letters: ", end = "")
            print(*misplaced, sep = ", ")
            print("Incorrect Letters: ", end = "")
            print(*wrong, sep = ", ")
            print()
            
            turns += 1
            
            if guess == word:
                success = True
                print(f'You got it! "{guess.capitalize()}" is the right word! Congratulations!')
                break
            
            print("You have " + str(maxturns - turns) + " turns left!")
            print()
    
    if success == False:
        print("You ran out of turns. Better luck next time!")
              

if __name__ == "__main__":
    main()
