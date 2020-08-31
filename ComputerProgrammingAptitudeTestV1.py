'''
Computer Programming Aptitude Test

The test has 26 questions and you will have 25 minutes to do them.
At the end of the test (when 25 minutes have elapsed),
you will be given a score. Please use SCRAP PAPER and a CALCULATOR for working
out answers. Please note that this is quite a demanding test.

Beau Seate
8/31/20

'''
import time


def main():
    instructions()
    #timer()
    
    
    




def instructions():
    
    print("The test has 26 questions and you will have 25 minutes to do them.")
    print("At the end of the test (when 25 minutes have elapsed), you will be given a score.")
    print("Please use SCRAP PAPER and a CALCULATOR for working out answers.")
    print("Please note that this is quite a demanding test.")
    print(input("\nPress enter to continue:"))
    
    
    









#====================Timer that counts down from 25 mins
def timer():
    seconds = 1500
    whenToStop = abs(int(seconds))
    while whenToStop > 0:
        m, s = divmod(whenToStop, 60)
        h, m = divmod(m, 60)
        timeLeft = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        print(timeLeft + "\r", end="")
        time.sleep(1)
        whenToStop -= 1



main()