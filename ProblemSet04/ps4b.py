from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#

def canConstructWord(word,hand):
    testHand = hand.copy()

    for letter in word:
        if testHand.get(letter, 0) == 0:
            return False
        testHand[letter] -= 1

    return True

def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    maximumScore = 0
    bestWord = None

    for word in wordList:
        if canConstructWord(word, hand):
            score = getWordScore(word, HAND_SIZE)
            if score > maximumScore:
                maximumScore = score
                bestWord = word

    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    numLettersLeft = calculateHandlen(hand)
    totalScore = 0

    while numLettersLeft > 0:
        print "Current Hand: ",
        displayHand(hand)
        word = compChooseWord(hand, wordList)
        if word == None:
            break
        else:
            score = getWordScore(word, HAND_SIZE)
            totalScore += score
            print '"'+word+'" earned '+str(score)+' points. Total: '+str(totalScore)+' points.'
            hand = updateHand(hand, word)
            numLettersLeft = calculateHandlen(hand)

    if numLettersLeft == 0:
        print "Ran out of letters."

    print 'Total score: '+str(totalScore)+' points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    lastHand = None
    while True:

        while True:
            option = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            if option == 'e':
                print "Goodbye!"
                return
            elif option == 'r' and lastHand == None:
                print "You have not played a hand yet. Please play a new hand first!"
            elif option in ['n', 'r']:
                break
            else:
                print "Invalid option."

        while True:
            player = raw_input("Enter u if you want to play the hand or c if you want the computer to play the hand: ")
            if player in ['u', 'c']:
                break
            print "Invalid option."

        if option == 'n':
            hand = dealHand(HAND_SIZE)
            lastHand = hand.copy()
        else:
            hand = lastHand.copy()

        if player == 'u':
            playHand(hand, wordList, HAND_SIZE)
        else:
            compPlayHand(hand, wordList)

        print
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


