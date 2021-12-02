"""My Integration Project"""
__author___ = "Kady Jackson"


# This is a program that helps COP1500 students study for the Python
# certification exam.
# Credit to Prof. Vanselow's POGILs which act as a great study guide.


def main():
    """The purpose of this function is to act as a table of contents for the
    program which includes calling the other functions."""
    # Welcome statement and introduction
    print("Welcome to your all inclusive certification study guide!")
    name = input("Your name: ")
    print("Hello,", name, ", you are going to do great! Let's get started!")

    # Initializing variables that will be used later on.
    num_correct = 0
    q_num = 0

    # Call to Functions - Table of Contents
    print(
        'Welcome to part 1, where you will answer 16 short response questions '
        'that will be self graded.'
        '\nGood luck!')
    ask_self_response_questions(q_num, num_correct)
    print(
        'Congrats, you made it to part 2, where you will answer 7 math related'
        ' questions that will be automatically '
        'graded.'
        '\nGood luck!')
    ask_math_questions(num_correct)
    closing_remarks()


# Defining a function that will run and ask the user the 16 free response
# questions.
def ask_self_response_questions(q_num, num_correct):
    """The purpose of this function is to ask the user the 16 short response
    questions, store their answers, and call the self_grade_answers function
    which grades the answers and keeping a running score.
    q_num - the question number that the user is on
    num_correct - the number the user currently has correct."""
    # Defining a string literal.
    q_num += 1
    answer = input("Question 1. What is a string literal? ")
    print("You said", answer)
    print(
        "The correct answer was a sequence of characters surrounded by double"
        " quotation marks.")
    # Calling the function that will prompt the user to self grade their
    # answer.
    num_correct = self_grade_score_answer(q_num, num_correct)

    # How to enter a new line.
    q_num += 1
    answer = input(
        "Question 2. What would you add to your code to cause the output to"
        " be entered onto the next line and indented? ")
    print("You said", answer)
    print(
        "The correct answer was a forward slash followed by the lowercase "
        "letter n.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # String literal application question.
    q_num += 1
    answer = input("Question 3. What do the commas do in a string literal? ")
    print("You said", answer)
    print("The correct answer was that commas add a space.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Application question
    q_num += 1
    answer = input("Question 4. What prompt and variable would you use if "
                   "you wanted the user to type something in that would then"
                   " be stored? ")
    print("You said", answer)
    print("The correct answer was to use variable = input().")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Clarifying the difference between using float and int.
    q_num += 1
    answer = input(
        "Question 5. What is the difference between a float and int? ")
    print("You said", answer)
    print(
        "The correct answer is that a float is a number with a decimal,"
        " and an int is a whole number.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # How to concatenate strings.
    q_num += 1
    answer = input("Question 6. Write a code that concatenates strings. ")
    print("You said", answer)
    print(
        "One example of a correct answer would be to do:\nfruit = 'apples' + '"
        " and ' + 'oranges' + ' are my ' + 'favorites'\nprint(fruit)"
        "\nCheck your code in PyCharm or IDLE to "
        "be sure your answer is right.")
    # Concatenating is a type of string operator, used by "+".
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Using string operators.
    q_num += 1
    print("Question 7. What would result from the following line of code:")
    answer = input("print('Hello' * 10) ")
    print("You said", answer)
    print(
        "The correct answer is that Hello would be repeated 10 times."
        "\nSee here:")
    print('Hello' * 10)
    # using the * in a string literal is also a string operator,
    # and it repeats the preceding statement however many times is specified
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Assignment statements, NOT equal signs.
    q_num += 1
    answer = input(
        "Question 8. What is the symbol '=' called when it is in a line of "
        "code? ")
    print("You said", answer)
    print("The correct answer is an assignment statement.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # How to use the int function.
    q_num += 1
    answer = input(
        "Question 9. What is the special function that you must use when you "
        "want to store a number as a variable "
        "and then have python run math between them? ")
    print("You said", answer)
    print(
        "The correct answer was to use the 'int' function. This stores the "
        "number as an integer.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Applying what you know into typing a code.
    q_num += 1
    print(
        "Question 10. Type a code using sep that will result in the"
        " following:")
    print('09', '14', '21', sep='-')
    answer = input()
    print("Your answer was", answer)
    print("An example of a correct answer would be to use:")
    print("print('09','14','21', sep='-')")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Applying what you know into typing a code.
    q_num += 1
    print(
        "Question 11. Type a code using end that will result in the"
        " following:")
    print('academi', end='@')
    answer = input('\nYour code: ')
    print("Your answer was", answer)
    print("An example of a correct answer would be to use")
    print("print('academi', end = '@')")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # What type of loop was used
    q_num += 1
    print(
        "Question 12. Look at the output below and type the loop that was used"
        " to create it.")
    for x in range(0, 20):
        print(x)
    answer = input("Type the code here: ")
    print("Your answer was", answer)
    print("An example of a correct answer would be to use")
    print("for x in range (0.20): \n    print(x)")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # User controls the loop
    q_num += 1
    while True:
        try:
            answer = int(input(
                "Question 13. Type a whole number integer in numeral form that"
                " is in the inclusive "
                "range of 5 and 20: "))
            break
        except ValueError:
            print(
                "Your input is either not a whole number or not in numeral"
                " form. Try again.")
    while answer < 5 or answer > 20:
        print(
            "Your answer is in the correct form however, it is incorrect."
            " Try again.")
        answer = int(input(
            "Type a number that is in the inclusive range of 5 and 20: "))
    if 5 <= answer <= 20:
        print(
            "Your answer is in the correct format and it is correct."
            " Great job!")
        num_correct = self_grade_score_answer(q_num, num_correct)

    # How was the above code ran?
    q_num += 1
    answer = input(
        "Question 14. Type a code using 'and' AND 'or' that made the above"
        " question successfully loop: ")
    print("You said:", answer)
    print("One correct answer was to use:\nwhile answer < 5 or answer > 20:"
          "\n   print('Your answer is in the correct form however, it is"
          " incorrect. Try again."
          "\n   answer = int(input('Type a number that is in the inclusive"
          " range of 5 and 20: '))"
          "\nif answer >= 5 and answer <= 20:"
          "\n   print('Your answer is in the correct format and it is correct."
          " Great job!')")
    print("Check your answer in IDLE or PyCharm.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # User controls the loop
    q_num += 1
    while True:
        try:
            answer = int(input(
                "Question 15. Type a whole number integer in numeral form that"
                " is greater than 0 and "
                "less than 20: "))
            break
        except ValueError:
            print(
                "Your input is either not a whole number or not in numeral"
                " form. Try again.")
    acceptable_answer = range(0, 20)
    while answer not in acceptable_answer:
        print(
            "Your answer is in the correct form, but it is incorrect."
            " Try again.")
        answer = int(
            input("Type a number that is greater than 0 and less than 20: "))
    if 20 > answer > 0:
        print(
            "Your answer is in the correct format and it is correct."
            " Great job!")
        num_correct = self_grade_score_answer(q_num, num_correct)

    # How was the above code ran?
    q_num += 1
    answer = input(
        "Question 16. Type a code using 'not' that made the above question"
        " successfully loop: ")
    print("You said:\n", answer)
    print("One correct answer was to do:\nacceptable_answer = range(0, 20)"
          "\nwhile answer not in acceptable_answer:"
          "\n   print('Your answer is in the correct form, but it is"
          " incorrect. Try again.')"
          "\n   answer = int(input('Type a number that is greater than 0 and"
          " less than 20: '))"
          "\nif 20 > answer > 0:"
          "\n   print('Your answer is in the correct format and it is"
          " correct. Great job!')")
    print("Check your answer in IDLE or PyCharm.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    print("Your final score for section one was ", num_correct, "/ 16.")

    return num_correct


# Defining a function that will ask the 7 math questions.
def ask_math_questions(num_correct):
    """The purpose of this function is to ask the 7 questions that require
    numerical answers and call ask_check_main_questions which automatically
    grades the 7 questions.
    num_correct - the number of answers the user currently has correct."""
    # Simple addition problem.
    q_num = 1
    line_of_code = "print(3+6): "
    correct_answer = int(9)
    reasoning = "This is because the + results in simple addition."
    # Calling the function that will ask the question and check the user's
    # input.
    num_correct = ask_check_math_problem(q_num, num_correct,
                                         line_of_code, correct_answer,
                                         reasoning)

    # Simple subtraction problem.
    q_num += 1
    line_of_code = "print(3-6): "
    correct_answer = int(-3)
    reasoning = "This is because the - results in simple subtraction."
    # Calling the function that will ask the question and check the user's
    # input.
    num_correct = ask_check_math_problem(q_num, num_correct,
                                         line_of_code, correct_answer,
                                         reasoning)

    # Simple multiplication problem.
    q_num += 1
    line_of_code = "print(3*6): "
    correct_answer = int(18)
    reasoning = "This is because the * results in simple multiplication."
    # Calling the function that will ask the question and check the user's
    # input.
    num_correct = ask_check_math_problem(q_num, num_correct,
                                         line_of_code, correct_answer,
                                         reasoning)

    # Simple division problem.
    q_num += 1
    line_of_code = "print(9/3): "
    correct_answer = int(3)
    reasoning = "This is because the / results in simple division."
    # Calling the function that will ask the question and check the user's
    # input.
    num_correct = ask_check_math_problem(q_num, num_correct,
                                         line_of_code, correct_answer,
                                         reasoning)

    # Floor division problem.
    q_num += 1
    line_of_code = "print(9//2): "
    correct_answer = int(4)
    reasoning = "This is because the // results in floor division. " \
                "Floor division returns the quotient without the remainder."
    # Calling the function that will ask the question and check the user's
    # input.
    num_correct = ask_check_math_problem(q_num, num_correct,
                                         line_of_code, correct_answer,
                                         reasoning)

    # Remainder quotient problem.
    q_num += 1
    question = "What number would result from the following line of code:"
    line_of_code = "print(9%2): "
    correct_answer = float(0.5)
    reasoning = "This is because the % results in the system returning just" \
                " the remainder of the quotient."
    # Calling the function that will ask the question and check the user's
    # input.
    num_correct = float_math_problem(q_num, num_correct, question,
                                     line_of_code, correct_answer, reasoning)

    # Exponential math problem.
    q_num += 1
    line_of_code = "print(3**6): "
    correct_answer = int(729)
    reasoning = "This is because the ** results in an exponential problem."
    # Calling the function that will ask the question and check the user's
    # input.
    num_correct = ask_check_math_problem(q_num, num_correct,
                                         line_of_code, correct_answer,
                                         reasoning)

    print("Your final score for section 2 was", num_correct, "/ 7.")


# Defining a function that will print the closing remarks.
def closing_remarks():
    """The purpose of this function is to print the closing remarks."""
    # Closing Remarks
    print("Congrats! You've finished the study guide.")
    print("Thanks for playing! Good luck on the exam!")


# Defining a program that will be used in the ask_check_math_problem function
# to automatically score users.
def score_answer(q_num, num_correct):
    """The purpose of this function is to grade the 7 questions that had
    numerical answers.
    q_num - the question number
    num_correct - the number the user currently has correct."""
    print("Great job! Your score is", num_correct, "/", q_num)
    return num_correct


# Defining a program that will be used for users to score themselves.
def self_grade_score_answer(q_num, num_correct):
    """The purpose of this function is to allow the user to self grade their
    responses to the 17 short response questions, since the answers inputted
    could vary largely but still be correct.
    q_num - the question number
    num_correct - the number the user currently has correct."""
    y_or_no = input(
        "Did you get this question right? \na. Yes \nb. No \nEnter a or b: ")
    if y_or_no == "a" or y_or_no == "A" or y_or_no == "Yes" or \
            y_or_no == "yes":
        num_correct += 1
        print("Great job! Your score is", num_correct, "/", q_num)
    elif y_or_no == "b" or y_or_no == "B" or y_or_no == "No" or \
            y_or_no == "no":
        print("Good try! Your score is", num_correct, "/", q_num)
    else:
        print("Invalid input. No point given.")
        print("Your score is", num_correct, "/", q_num)
    return num_correct
    # do not add == self_grade_score_answer(q_num, num_correct) here


# Defining a function that can ask for an answer to a math problem, accept
# an answer, and evaluate the answer.
def ask_check_math_problem(q_num, num_correct, line_of_code,
                           correct_answer, reasoning):
    """The purpose of this function is to ask the math related questions,
    store the users answer as an integer, allow them to retry if their
    answer was not correct, and keeps a running score of the number correct
    once they get the right answer.
    q_num - the question number
    num_correct - the number the user currently has correct
    line_of_code - the line of that code that the user has to know the
    result of
    correct_answer - the correct answer to the line of code, and
    reasoning - the explanation for the correct answer."""
    question = "What number would result from the following line of code: "
    print("Question", q_num, ".")
    print(question)
    while True:
        try:
            answer = int(input(line_of_code))
            break
        except ValueError:
            print(
                "Your input is either not a whole number or not in numeral "
                "form. Try again.")
    print("You said", answer)
    while answer != correct_answer:
        if answer > correct_answer:
            print(
                "Your answer is a little higher than the correct. Try again.")
            answer = int(input(line_of_code))
        elif answer < correct_answer:
            print("Your answer is a little lower than the correct. Try again.")
            answer = int(input(line_of_code))
    if answer == correct_answer:
        print("The answer was", correct_answer)
        print("Your answer is correct!", reasoning)
    num_correct += 1
    # Function call to score_answer, which will automatically score the
    # user's response.
    num_correct = score_answer(q_num, num_correct)
    return num_correct


# Defining a function for a math problem, however the input must be a decimal.
def float_math_problem(q_num, num_correct, question, line_of_code,
                       correct_answer, reasoning):
    """The purpose of this function is to ask the math related questions,
    store the users answer as a decimal, allows them to retry if their
    answer was incorrect, and scores their answer once they get the right
    answer, while keeping a running score.
    q_num - the question number,
    num_correct - the number the user currently has correct
    question - the sentence containing the question
    line_of_code - the line of that code that the user has to know the
    result of
    correct_answer - the correct answer to the line of code, and
    reasoning - the explanation for the correct answer"""
    print("Question", q_num, ".", question)
    answer = float(input(line_of_code))
    print("You said", answer)
    while answer != correct_answer:
        if answer > correct_answer:
            print(
                "Your answer is a little higher than the correct. Try again.")
            answer = int(input(line_of_code))
        elif answer < correct_answer:
            print("Your answer is a little lower than the correct. Try again.")
            answer = int(input(line_of_code))
    if answer == correct_answer:
        print("The answer was", correct_answer)
        print("Your answer is correct!", reasoning)
        num_correct += 1
        num_correct = score_answer(q_num, num_correct)
    return num_correct


# Call to main
if __name__ == '__main__':
    main()
