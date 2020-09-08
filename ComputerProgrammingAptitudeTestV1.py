'''
Computer Programming Aptitude Test

The test has 26 questions and you will have 25 minutes to do them.
You will see how much time you have left after every question. 
At the end of the test (when 25 minutes have elapsed),
you will be given a score. Please use SCRAP PAPER and a CALCULATOR for working
out answers. Please note that this is quite a demanding test.

Beau Seate
9/2/20
'''
import threading
import time
import sys
import os


#==============Main program
def main():
    #==========Declaring global variables (correct answers/stored answers)
    global ANSWER_CHOICES
    ANSWER_CHOICES = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f"]#Valid answer selections
    
    exSA1 = ""#User stored answer from return 
    exC1 = "D"#Correct answer form answer key
    
    exSA2 = ""
    exC2 = "A"
    
    exSA3 = ""
    exC3 = "F"
    
    
    #==========Program start
    instructions()
    timerThread = threading.Thread(target = timer)
    timerThread.start()
    exSA1 = exQ1()
    exSA2 = exQ2()
    exSA3 = exQ3()
    
   
#===================Import OS to clear screen to declutter window
def clearScreen():
    #=================Checks for OS to issue correct clear screen command
    os.system("cls" if os.name == 'nt' else 'clear')

#=========================Prints instructions before test is taken
def instructions():
        print("\nThis test has 26 questions and you will have 25 minutes to do them.")
        print("You will see how much time you have left after each question.")
        print("At the end of the test (or when 25 minutes have elapsed), you will be given a score.")
        print("Please use SCRAP PAPER and a CALCULATOR for working out answers.")
        print("Please note that this is quite a demanding test.")
        print("The test will start with three easy example questions which will not be marked or timed.")
        print("You cannot change your answers after submitting.")
        input("\nPress enter to start practice problem 1:")
        clearScreen()#Clear screen method

#=========================Display results of test and what they mean
def displayResults(userScore):
    print()
    

def displayTable():
    from tabulate import tabulate
    null = ""
    l = [["#1", 9, 7, 8, 4, null, null], ["#2", 8, 2, 3, 7, null, null], ["#3", 11, 1, 5, 6, null, null], ["#4",13, 9, 6, 3, null, null]]
    table = tabulate(l, headers=[null,"A","B","C","D","E","F"], tablefmt="orgtbl")
    print(table)


#====================Timer that counts down from 25 mins
def timer():
    global myTime
    global timeLeft
    myTime = 1500
    while myTime > 0:
        m, s = divmod(myTime, 60)
        h, m = divmod(m, 60)
        timeLeft = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        time.sleep(1)
        myTime -= 1
    print("\nOut of time!")


#======================Input validation void method
def checkAnswer(exA):
    result = any(ele in exA for ele in ANSWER_CHOICES)#Result gives boolean check for "True" return
    while(bool(result) == False or 1 < len(exA)):#If the result return is "False" or length of string > 1
        exA = input(str("Please enter a valid letter choice: "))#Input validation
        result = any(ele in exA for ele in ANSWER_CHOICES)#Result gives boolean check for "True" return
        
        
        
#=======================Example question 1
def exQ1():
    '''
    :rtype: exA
    '''
    exA = ""#Variable to store user input
    if myTime > 0:#While there is time left
        print("\n" + timeLeft)#Print time left for user
    
    print("\nEXAMPLE 1 (This does not count to your overall score)\n\n1) Maggie thought of a number, added 7, multiplied by 3,",end=" ")
    print("took away 5, and divided by 4 to give an answer of 7.\n\nWhat was her starting number?")
    print("\nA. 1\nB. 2\nC. 3\nD. 4\nE. 5\nF. 6")#Answer option menu
    exA = input(str("\n\n\nYour answer: "))#Ask user for letter answer
    checkAnswer(exA)
    while myTime > 0:#While there is time left
        print(timeLeft + "\r", end="")#Print time left for user
        time.sleep(1)#Wait a second for user to check time
        if(exA != ""):#If answer has an input
            clearScreen()#clearScreen method erases screen
            break#break loop
    
    return exA#Return user answer

#====================Example question 2
def exQ2():
    '''
    :rtype: exA
    '''
    exA = ""
    if myTime > 0:#While there is time left
        print("\n" + timeLeft)#Print time left for user
        
    print("\nEXAMPLE 2 (This does not count to your overall score) (Look at the table)\n\nIn these questions, the", end=" ")
    print("coordinates (e.g. A1) of a square refer to the number in the square, e.g. A1 = 9")
    print("\n\n")
    displayTable()
    print("\n\n2) What is B1 + C2?")
    print("\nA. 10\nB. 11\nC. 12\nD. 13\nE. 14\nF. None of the Above")
    exA = input(str("\n\n\nYour answer: "))
    checkAnswer(exA)
    while myTime > 0:
        print(timeLeft + "\r", end="")
        time.sleep(1)
        if(exA != ""):
            clearScreen()
            break    
    
    return exA

#=====================Example question 3
def exQ3():
    '''
    :rtype: exA
    '''
    exA = ""
    if myTime > 0:#While there is time left
        print("\n" + timeLeft)#Print time left for user
        
    print("\nFINAL EXAMPLE: THE TIMED TEST WILL BEGIN AFTER THIS QUESTION.\n\nIn these questions, the", end=" ")
    print("coordinates (e.g. A1) of a square refer to the number in the square, e.g. A1 = 9")
    print("\n\n")
    displayTable()
    print("\n\n3) Multiply A1 by B2. Put the result in E1. Now divide E1 by D4.\n\nWhat is the answer?")
    print("\nA. 1\nB. 2\nC. 3\nD. 4\nE. 5\nF. None of the Above")
    exA = input(str("\n\n\nYour answer: "))
    checkAnswer(exA)
    while myTime > 0:
        print(timeLeft + "\r", end="")
        time.sleep(1)
        if(exA != ""):
            clearScreen()
            break    
    
    return exA



main()