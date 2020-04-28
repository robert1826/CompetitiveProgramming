import io
import os
import sys
from atexit import register

##################################### Flags          #####################################
DEBUG = True
STRESSTEST = False

##################################### IO             #####################################

if not DEBUG:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.stdout = io.BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

tokens = []
tokens_next = 0


def nextStr():
    global tokens, tokens_next
    while tokens_next >= len(tokens):
        tokens = input().split()
        tokens_next = 0
    tokens_next += 1

    if type(tokens[tokens_next - 1]) == str:
        return tokens[tokens_next - 1]
    return tokens[tokens_next - 1].decode()


def nextInt():
    return int(nextStr())


def nextIntArr(n):
    return [nextInt() for i in range(n)]


def print(*argv, end='\n'):
    for arg in argv:
        sys.stdout.write((str(arg) + ' ').encode())
    sys.stdout.write(end.encode())


##################################### Helper Methods #####################################
def genTestCase():
    raise NotImplementedError


def bruteforce(a):
    raise NotImplementedError


def doStressTest():
    while True:
        curTest = genTestCase()
        mySoln = solve(curTest)
        bruteforceSoln = bruteforce(curTest)
        if mySoln != bruteforceSoln:
            print('### Found case ###')
            print(curTest)
            print(f'{mySoln} should have been: {bruteforceSoln}')
            return


def solve(a):
    raise NotImplementedError


##################################### Driver         #####################################

if __name__ == "__main__":
    if not DEBUG and STRESSTEST:
        raise Exception('Wrong flags!')

    if STRESSTEST:
        doStressTest()
    else:
        ### Read input here
        a = nextIntArr(nextInt())
        res = solve(a)
        print(res)
        sys.stdout.flush()
