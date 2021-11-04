# Kady Jackson
# A program that helps COP1500 students study for the Python certification exam.
# Credit to Prof. Vanselow's POGILs which act as a great study guide.


def main():
    # Welcome statement and introduction
    print("Welcome to your all inclusive certification study guide!")
    name = input("Your name: ")
    print("Hello,", name, ", you are going to do great! Let's get started!")

    # Initializing variables that will be used later on.
    num_correct = 0
    q_num = 0

    # Calling Functions - Table of Contents
    ask_self_response_questions(q_num, num_correct)
    # Reinitializing q_num to 0 to separate the number of questions in the two sections.
    q_num = 0
    ask_math_questions(num_correct)
    closing_remarks(num_correct)


# Defining a function that will run and ask the user the 16 free response questions.
def ask_self_response_questions(q_num, num_correct):
    # Defining a string literal.
    q_num += 1
    answer = input("Question 1. What is a string literal? ")
    print("You said", answer)
    print("The correct answer was a sequence of characters surrounded by double quotation marks.")
    # Calling the function that will prompt the user to self grade their answer.
    num_correct = self_grade_score_answer(q_num, num_correct)

    # How to enter a new line.
    q_num += 1
    answer = input("Question 2. What would you add to your code to cause the output to be "
                   "entered onto the next line and indented? ")
    print("You said", answer)
    print("The correct answer was a forward slash followed by the lowercase letter n.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # String literal application question.
    q_num += 1
    answer = input("Question 3. What do the commas do in a string literal? ")
    print("You said", answer)
    print("The correct answer was that commas add a space.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Application question
    q_num += 1
    answer11 = input("Question 4. What prompt and variable would you use if "
                     "you wanted the user to type something in that would then be stored? ")
    print("You said", answer)
    print("The correct answer was to use variable = input().")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Clarifying the difference between using float and int.
    q_num += 1
    answer = input("Question 5. What is the difference between a float and int? ")
    print("You said", answer)
    print("The correct answer is that a float is a number with a decimal, and an int is a whole number.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # How to concatenate strings.
    q_num += 1
    answer = input("Question 6. Write a code that concatenates two strings. ")
    print("You said", answer)
    print("The first line of your code should have a variable name, then an equal sign, "
          "then one word in quotations, plus another word in quotations. "
          "Don't forget about the spaces. The next line should have a print statement with just the variable name.")
    # Concatenating is a type of string operator, used by "+".
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Using string operators.
    q_num += 1
    print("Question 7. What would result from the following line of code:")
    answer = input("print('Hello' * 10) ")
    print("You said", answer)
    print("The correct answer is that Hello would be repeated 10 times.")
    # using the * in a string literal is also a string operator,
    # and it repeats the preceding statement however many times is specified
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Assignment statements, NOT equal signs.
    q_num += 1
    answer = input("Question 8. What is the symbol '=' called when it is in a line of code? ")
    print("You said", answer)
    print("The correct answer is an assignment statement.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # How to use the int function.
    q_num += 1
    answer = input(
        "Question 9. What is the special function that you must use when you want to store a number as a variable "
        "and then have python run math between them? ")
    print("You said", answer)
    print("The correct answer was to use the int function. This stores the number as an integer.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Applying what you know into typing a code.
    q_num += 1
    print("Question 10. Type a code using sep that will result in the following:")
    print("09-14-21")
    answer = input()
    print("Your answer was", answer)
    print("An example of a correct answer would be to use:")
    print("print('09','14','21', sep='-')")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # Applying what you know into typing a code.
    q_num += 1
    print("Question 11. Type a code using end that will result in the following:")
    print("academi@")
    answer = input()
    print("Your answer was", answer)
    print("An example of a correct answer would be to use")
    print("print('academi', end = '@')")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # What type of loop was used
    q_num += 1
    print("Question 12. Look at the output below and type the loop that was used to create it.")
    for x in range(0, 20):
        print(x)
    answer = input("Type the code here: ")
    print("Your answer was", answer)
    print("An example of a correct answer would be to use")
    print("for x in range (0.20): print(x)")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # User controls the loop
    q_num += 1
    answer = int(input("Question 13. Type a number that is in the inclusive range of 5 and 20: "))
    while answer < 5 or answer > 20:
        print("Your answer is not correct. Try again.")
        answer = int(input("Type a number that is in the inclusive range of 5 and 20: "))
    if answer >= 5 and answer <= 20:
        print("Your answer is valid.")
        num_correct = self_grade_score_answer(q_num, num_correct)

    # How was the above code ran?
    q_num += 1
    answer = input("Question 14. Type a code using 'and' and 'or' that made the above question successfully loop: ")
    print("One correct answer was to use 'while answer < 5 or answer > 20:' and 'if answer >= 5 and answer <= 20:'")
    print("Check your answer in IDLE or PyCharm.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    # User controls the loop
    q_num += 1
    answer = int(input("Question 15. Type a number that is greater than 0 and less than 20: "))
    acceptable_answer = range(0, 20)
    while answer not in acceptable_answer:
        print("Your answer is not correct. Try again.")
        answer = int(input("Type a number that is greater than 0 and less than 20: "))
    if answer < 20 and answer > 0:
        print("Your answer is valid.")
        num_correct = self_grade_score_answer(q_num, num_correct)

    # How was the above code ran?
    q_num += 1
    answer = input("Question 16. Type a code using 'not' that made the above question successfully loop: ")
    print("One correct answer was to use assign a variable 'acceptable answer = range(0,20)'. "
          "Then use a while loop 'while answer not in acceptable_answer:'"
          "And finally, use an if statement 'if answer < 20 and answer > 0:'")
    print("Check your answer in IDLE or PyCharm.")
    num_correct = self_grade_score_answer(q_num, num_correct)

    print("Your final score for section one was ", num_correct, "/ 16.")

    return num_correct


def ask_math_questions(num_correct):
    # Simple addition problem.
    q_num = 1
    question = "What number would result from the following line of code: "
    line_of_code = "print(3+6): "
    correct_answer = int(9)
    reasoning = "This is because the + results in simple addition."
    # Calling the function that will ask the question and check the user's input.
    num_correct = ask_check_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning)

    # Simple subtraction problem.
    q_num += 1
    question = "What number would result from the following line of code:"
    line_of_code = "print(3-6): "
    correct_answer = int(-3)
    reasoning = "This is because the - results in simple subtraction."
    # Calling the function that will ask the question and check the user's input.
    num_correct = ask_check_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning)

    # Simple multiplication problem.
    q_num += 1
    question = "What number would result from the following line of code:"
    line_of_code = "print(3*6): "
    correct_answer = int(18)
    reasoning = "This is because the * results in simple multiplication."
    # Calling the function that will ask the question and check the user's input.
    num_correct = ask_check_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning)

    # Simple division problem.
    q_num += 1
    question = "What number would result from the following line of code:"
    line_of_code = "print(9/3): "
    correct_answer = int(3)
    reasoning = "This is because the / results in simple division."
    # Calling the function that will ask the question and check the user's input.
    num_correct = ask_check_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning)

    # Floor division problem.
    q_num += 1
    question = "What number would result from the following line of code:"
    line_of_code = "print(9//2): "
    correct_answer = int(4)
    reasoning = "This is because the // results in floor division. " \
                "Floor division returns the quotient without the remainder."
    # Calling the function that will ask the question and check the user's input.
    num_correct = ask_check_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning)

    # Remainder quotient problem.
    q_num += 1
    question = "What number would result from the following line of code:"
    line_of_code = "print(9%2): "
    correct_answer = float(0.5)
    reasoning = "This is because the % results in the system returning just the remainder of the quotient."
    # Calling the function that will ask the question and check the user's input.
    num_correct = float_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning)

    # Exponential math problem.
    q_num += 1
    question = "What number would result from the following line of code:"
    line_of_code = "print(3**6): "
    correct_answer = int(729)
    reasoning = "This is because the ** results in an exponential problem."
    # Calling the function that will ask the question and check the user's input.
    num_correct = ask_check_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning)

    print("Your final score for section 2 was", num_correct, "/ 7.")


# Defining a function that will print the closing remarks.
def closing_remarks(num_correct):
    # Closing Remarks
    print("Congrats! You've finished the study guide.")
    print("Thanks for playing! Good luck on the exam!")


# Defining a program that will be used in the ask_check_math_problem function to automatically score users.
def score_answer(q_num, num_correct):
    print("Great job! Your score is", num_correct, "/", q_num)
    return num_correct


# Defining a program that will be used for users to score themselves.
def self_grade_score_answer(q_num, num_correct):
    y_or_no = input("Did you get this question right? Input 'y' for yes or 'n' for no:")
    if y_or_no == "y":
        num_correct += 1
        print("Great job! Your score is", num_correct, "/", q_num)
    else:
        print("Your score is", num_correct, "/", q_num)
    return num_correct
    # do not add == self_grade_score_answer(q_num, num_correct) here


# Defining a function that can ask for an answer to a math problem, accept an answer, and evaluate the answer.
def ask_check_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning):
    question = "What number would result from the following line of code: "
    print("Question", q_num, ".")
    print(question)
    answer = int(input(line_of_code))
    print("You said", answer)
    while answer != correct_answer:
        if answer > correct_answer:
            print("Your answer is a little higher than the correct. Try again.")
            answer = int(input(line_of_code))
        elif answer < correct_answer:
            print("Your answer is a little lower than the correct. Try again.")
            answer = int(input(line_of_code))
    if answer == correct_answer:
        print("The answer was", correct_answer)
        print("Your answer is correct!", reasoning)
    num_correct += 1
    # Function call to score_answer, which will automatically score the user's response.
    num_correct = score_answer(q_num, num_correct)
    return num_correct


# Defining a function for a math problem, however the input must be a decimal.
def float_math_problem(q_num, num_correct, question, line_of_code, correct_answer, reasoning):
    print("Question", q_num, ".", question)
    answer = float(input(line_of_code))
    print("You said", answer)
    while answer != correct_answer:
        if answer > correct_answer:
            print("Your answer is a little higher than the correct. Try again.")
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


main()
