#
# AverageNumberOfWords.py
#
# Your instructor has provided you access to a file named text.txt. The text that is 
# in the file is stored as one sentence per line. Write a program that reads the file’s 
# contents and calculates the average number of words per sentence.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called calculateAverageNumberOfWordsPerSentence.  This function will not be passed anything. 
# The function function will read the text file, calculate and return the average number of words per sentence: 
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateAverageNumberOfWordsPerSentence(textFile):
        total_words = 0
        sentence_count = 0
        with open(textFile, "r") as file:
                for line in file:
                        sentences = line.split()
                        sentence_count += 1
                        for sentence in sentences:
                                print(sentence)
                                word_count = len(sentence.split()) # make a word in an array and get the len of array
                                total_words += word_count
                                

        print(total_words)
        print(sentence_count)

        average_words = total_words / sentence_count 
        
        return average_words
	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#


def main():

        textFile = input("What is the name of the text file that you would like to calculate the average number of words? ")

        averageNumberOfWordsPerSentence = calculateAverageNumberOfWordsPerSentence(textFile)
        print("The average number of words per sentence in text.txt is", averageNumberOfWordsPerSentence)

main()
