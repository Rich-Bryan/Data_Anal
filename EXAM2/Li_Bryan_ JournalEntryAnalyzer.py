#################################################################################################################
#                                                                                                               #
# JournalEntryAnalyzer.py                                                                                       #
#                                                                                                               #
# Write a program that analyzes a journal entry to give feedback on emotional content and sentence structure.   #
# Create two functions: one to count the number of positive and negative words, and another to count the        #
# number of sentences. The program should allow the user to enter a journal entry and then display the number   #
# of positive words, negative words, and sentences.                                                             #
#                                                                                                               #
# The main program has been provided for you.  The main program will get some input from the user, invoke one   #
# or more functions to do the actual work, and display some output.  Your job is to create/update the functions #
# that do the actual work and return the results to the main program.                                           #
#                                                                                                               #
# Create a function called countEmotionalWords. This function takes a journal entry as a string and returns     #
# two counts: the number of positive words and the number of negative words.  Use the following lists:          #
#   Positive Words: ["happy", "joy", "love", "excited", "hopeful", "grateful"]                                  #
#   Negative Words: ["sad", "angry", "upset", "frustrated", "hopeless", "disappointed"]                         #
#                                                                                                               #
#################################################################################################################
#                                                                                                               #
# Please note that the function declaration has been provided for you. Do not change the function declaration   #
# in any way. Write the code that makes up the function without altering the function declaration. For graded   #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work. This will be discussed in class.                                                #
#                                                                                                               #
#################################################################################################################

def countEmotionalWords(journalEntry):
    positive_words = ["happy", "joy", "love", "excited", "hopeful", "grateful"]
    negative_words = ["sad", "angry", "upset", "frustrated", "hopeless", "disappointed"]
    positive_count = 0
    negative_count = 0

    arr = journalEntry.split()
    for word in arr:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
    return positive_count, negative_count



#################################################################################################################
# Create a function called countSentences. This function takes a journal entry as a string and returns          #
# the number of sentences by counting the punctuation marks ".", "!" and "?" as sentence boundaries.            #
#################################################################################################################

def countSentences(journalEntry):
    ending = {".","!","?"}
    lazy_count = 0
    lazy_count += journalEntry.count(".")
    lazy_count += journalEntry.count("!")
    lazy_count += journalEntry.count("?")
    return lazy_count

    arr = journalEntry.split()
    count = 0
    print(arr)
    #cna i just use slice and check the end if it end with ending? 
    for word in arr:
        if word[-1] in ending:
            count += 1 

    return count


    

#################################################################################################################
# The main program starts here through the end of the file. You should not be making any changes to the main    #
# program. You should only be creating/updating the functions defined above.                                    #
#################################################################################################################

def main():
    journalEntry = input("Enter a journal entry and press 'Enter' to analyze its emotional content and structure: ")
    positiveCount, negativeCount = countEmotionalWords(journalEntry)
    sentenceCount = countSentences(journalEntry)
    
    print("Number of positive words:   ", positiveCount)
    print("Number of negative words:   ", negativeCount)
    print("Number of sentences:        ", sentenceCount)

main()
