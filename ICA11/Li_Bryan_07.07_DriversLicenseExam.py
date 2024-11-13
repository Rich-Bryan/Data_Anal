#
# DriversLicenseExam.py
#
# The local driver’s license office has asked you to create an application that grades the 
# written portion of the driver’s license exam. The exam has 20 multiple-choice questions. 
#
# Here are the correct answers:
#
#    A
#    C
#    A
#    A
#    D
#    B
#    C
#    A
#    C
#    B
#    A
#    D
#    C
#    A
#    D
#    C
#    B
#    B
#    D
#    A
# 
# Your program should store these correct answers in a list. The program should read the student’s 
# answers for each of the 20 questions from a text file and store the answers in another list. 
# (Create your own text file to test the application.) After the student’s answers have been read 
# from the file, the program should display a message indicating whether the student passed or failed 
# the exam. (A student must correctly answer 15 of the 20 questions to pass the exam.) It should then 
# display the total number of correctly answered questions, the total number of incorrectly answered 
# questions, and a list showing the question numbers of the incorrectly answered questions. 
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called gradeExam.  This function will be passed both the answer key (as a list) and the name
# of a file that has an applicant's answers to the exam.  The function will read the file into a list and compare  
# the answers in the file to the answer key.  The function will display the information described above and will
# return the percentage of questions answered correctly.  Make sure you return the percentage of questions answered
# correctly.  For example, if they scored 80% on the exam, the function needs to return the value 80, not the value
# .8: 
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def gradeExam(applicantsAnswers,answerKey):
    with open(applicantsAnswers, 'r') as file:
        student_answers = []
        for line in file:
                student_answers.append(line.strip())
        print(student_answers)

    correct_count = 0
    incorrect_questions = []

    # check each value from the real answer with student answer
    for i in range(len(answerKey)):
        if student_answers[i] == answerKey[i]:
            correct_count += 1
        else:
            incorrect_questions.append(i + 1)  

    
    incorrect_count = len(incorrect_questions)
    
    result = ""
    if correct_count >= 15:
        result = "Passed"
    else:
        result = "Failed"


    print(f"Result: {result}")
    print(f"Total correct answers: {correct_count}")
    print(f"Total incorrect answers: {incorrect_count}")
    if incorrect_questions:
        print(f"Questions answered incorrectly: {incorrect_questions}")
    
    percentage_correct = (correct_count / len(answerKey)) * 100
    return percentage_correct

		
#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        answerKey = ['A',
                     'C',
                     'A',
                     'A',
                     'D',
                     'B',
                     'C',
                     'A',
                     'C',
                     'B',
                     'A',
                     'D',
                     'C',
                     'A',
                     'D',
                     'C',
                     'B',
                     'B',
                     'D',
                     'A']


        applicantsAnswers = input("Please enter the name of the file that has the applicant's answers: ")
        percentCorrect = gradeExam(applicantsAnswers,answerKey)
        print("The applicant got " + str(percentCorrect) + "% on the exam")

main()
