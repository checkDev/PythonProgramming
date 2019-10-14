import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    i = 0
    while i < 100 :
        sum = 0
        i = i +1
        sum = sum + random.randint(1,6)
        sum = sum + random.randint(1,6)
        print(sum,end = '\n')
