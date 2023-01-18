from InterviewPracticeQuestion import tenToTheN

def testTenToTheN(N):
    ans = tenToTheN()

    # Find Correct Answer
    if N%1 != 0:
        corAns = None
    elif N <= 0:
        corAns = None
    else:
        corAns = 10**N
        
    if ans == corAns:
        result = "Pass"
    else:
        result = "Fail"
    print(result + ". Input = " + str(N) + ", Result = " + str(ans) + ", Expected Result = " + str(corAns))


testTenToTheN(1)
testTenToTheN(4)
testTenToTheN(3.75)
testTenToTheN(0)
testTenToTheN(-5)
