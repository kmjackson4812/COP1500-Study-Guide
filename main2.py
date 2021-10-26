#Kady Jackson
#A program that helps COP1500 students study for the Python certification exam
#shoutout to Prof. Vanselow's POGILs which act as a great study guide, I will also use Coursera in the future
print("Welcome to your all inclusive certification study guide!")
name = input("Your name: ")
print("Hello,",name,", you are going to do great! Let's get started!")

#Defining a string literal.
answer = input("Question 1. What is a string literal?" )
print("You said",answer)
print("The correct answer was a sequence of characters surrounded by double quotation marks.")

#How to enter a new line.
answer = input("Question 2. What would you add to your code to cause the output to be entered onto the next line and indented?")
print("You said",answer)
print("The correct answer was a forward slash followed by the lowercase letter n.")

#Defining a function that can ask for an answer to a math problem, accept an answer, and evaluate the answer.
def mathproblem():
    print("Question",qnum,".",question)
    answer = int(input(lineofcode))
    print("You said",answer)
    while answer != canswer:
        print("Your answer is incorrect. Try again.")
        answer = int(input(lineofcode))
    if answer == canswer:
        print("The answer was",canswer)
        print("Your answer is correct!",reasoning)

#Simple addition problem.
qnum = 3
question = "What number would result from the following line of code:"
lineofcode = "print(3+6): "
canswer = int(9)
reasoning = "This is because the + results in simple addition."

mathproblem()

#Simple subtraction problem.
qnum += 1
question = "What number would result from the following line of code:"
lineofcode = "print(3-6): "
canswer = int(-3)
reasoning = "This is because the - results in simple subtraction."

mathproblem()

#Simple multiplication problem.
qnum +=1
question = "What number would result from the following line of code:"
lineofcode = "print(3*6): "
canswer = int(18)
reasoning = "This is because the * results in simple multiplication."

mathproblem()

#Simple division problem.
qnum +=1
question = "What number would result from the following line of code:"
lineofcode = "print(9/3): "
canswer = int(3)
reasoning = "This is because the / results in simple division."

mathproblem()

#Floor division problem.
qnum +=1
question = "What number would result from the following line of code:"
lineofcode = "print(9//2): "
canswer = int(4)
reasoning = "This is because the // results in floor division. Floor division returns the quotient without the remainder."

mathproblem()

#Defining a function for a math problem, however the input must be a decimal.
def floatmathproblem():
    print("Question",qnum,".",question)
    answer = float(input(lineofcode))
    print("You said",answer)
    while answer != canswer:
        print("Your answer is incorrect. Try again.")
        answer = float(input(lineofcode))
    if answer == canswer:
        print("The answer was",canswer)
        print("Your answer is correct!",reasoning)
    
#Remainder quotient problem.
qnum +=1
question = "What number would result from the following line of code:"
lineofcode = "print(9%2): "
canswer = float(0.5)
reasoning = "This is because the % results in the system returning just the remainder of the quotient."

floatmathproblem()

#Exponential math problem.
qnum +=1
question = "What number would result from the following line of code:"
lineofcode = "print(3**6): "
canswer = int(729)
reasoning = "This is because the ** results in an exponential problem."

mathproblem()

#String literal application question.
answer = input("Question 10. What do the commas do in a string literal?")
print("You said", answer)
print("The correct answer was that commas add a space.")

#applications
answer11 = input("Question 11. What prompt and variable would you use if you wanted the user to type something in that would then be stored?")
print("You said", answer)
print("The correct answer was to use variable = input().")

#Clarifying the difference between using float and int.
answer = input("Question 12. What is the difference between a float and int?")
print("You said", answer)
print("The correct answer is that a float is a number with a decimal, and an int is a whole number.")

#How to contatenate strings.
answer = input("Question 13. Write a code that concatenates two strings.")
print("You said", answer)
print("The first line of your code should have a variable name, then an equal sign, then one word in quotations, plus another word in quotations. Don't forget about the spaces. The next line should have a print statement with just the variable name.")
#Concatanating is a type of string operater, used by "+".

#Using string operators.
print("Question 14. What would result from the following line of code:")
answer = input("print('Hello' * 10)")
print("You said", answer)
print("The correct answer is that Hello would be repeated 10 times.")
#using the * in a string literal is also a string operator, and it repeats the preceding statement however many times is specified

#Assignment statements, NOT equal signs.
answer = input("Question 15. What is it called when a line of code using a =")
print("You said", answer)
print("The correct answer is an assignment statement.")

#How to use the int function.
answer = input("Question 16. What is the special function that you must use when you want to store a number as a variable and then have python run math between then?")
print("You said", answer)
print("The correct answer was to use the int function. This stores the number as an integer.")

#Applying what you know into typing a code.
print("Question 17. Type a code using sep that will result in the following")
answer = input("09-14-21")
print("Your answer was", answer)
print("An example of a correct answer would be to use")
print("print('09','14','21', sep='-')")

#Applying what you know into typing a code.
print("Question 18. Type a code using end that will result in the following")
answer = input("academi@")
print("Your answer was", answer)
print("An example of a correct answer would be to use")
print("print('academi', end = '@')")
