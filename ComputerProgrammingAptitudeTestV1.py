'''
Computer Programming Aptitude Test

The test has 26 questions and you will have 25 minutes to do them.
You will see how much time you have after every question. 
At the end of the test (when 25 minutes have elapsed),
you will be given a score. Please use SCRAP PAPER and a CALCULATOR for working
out answers. Please note that this is quite a demanding test.

Beau Seate
8/31/20

'''
import threading
import time
import sys

#==============Main program
def main():
    #==========Declaring global variables (correct answers/stored answers)
    exSA1 = " "#User stored answer from return
    exC1 = "D"#Correct answer form answer key
    
    
    #==========Program start
    instructions()
    clearScreen()
    exSA1 = exQ1()
    if(exSA1 == exC1):#If stored answer is the correct answer
        print("\nCorrect!")
        input("Press enter to cont:")
    else:
        print("\nIncorrect!")
        input()
    
    
    
    
    
    



#===================Import OS to clear screen to declutter
def clearScreen():
    import os
    
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







#====================Timer that counts down from 25 mins
def timer():
    myTime = 10
    while myTime > 0:
        m, s = divmod(myTime, 60)
        h, m = divmod(m, 60)
        timeLeft = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        time.sleep(1)
        myTime -= 1


def exQ1():
    exA1 = ""
    print("EXAMPLE\n1) Maggie thought of a number, added 7, multiplied by 3,",end=" ")
    print("took away 5, and divided by 4 to give an answer of 7.\n\nWhat was her starting number?")
    print("\nA. 1\nB. 2\nC. 3\nD. 4\nE. 5\nF. 6")
    exA1 = input("\n\nYour answer: ")
    
    return(exA1)


main()