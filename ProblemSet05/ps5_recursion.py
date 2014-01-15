# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if aStr == "":
        return ""
    else:
        return reverseString(aStr[1:]) + aStr[0]

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == "":
        return True
    elif word == "":
        return False
    elif x[0] == word[0]:
        return x_ian(x[1:], word[1:])
    else:
        return x_ian(x, word[1:])

#
# Problem 5: Typewriter
#
def getWords(text):
    words = text.split(' ')
    return words

def insertNewlinesRec(words, lineLength, currentLineLength, formattedText):
    if words == []:
        return formattedText
    word = words[0]
    wordLength = len(word)
    if currentLineLength < lineLength:
        formattedText += word+' '
        return insertNewlinesRec(words[1:], lineLength, currentLineLength+wordLength+1, formattedText)
    else:
        formattedText += '\n'
        return insertNewlinesRec(words, lineLength, 0,formattedText)

def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    lineLength: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    return insertNewlinesRec(getWords(text), lineLength, 0, "")