from random import randint
from pathlib import Path
import time

operators = ['+', '-', '*', '/']
difficulty = 0

def generateAddEquation():
    left = randint(2*difficulty, 20*difficulty-1)
    right = randint(1, 20*difficulty-left)

    if (randint(1, 5) > 5 - difficulty):
        left = left * 10
        right = right * 10

    return (str(left) + ' + ' + str(right) + ' = ', left + right)

def generateMinusEquation():
    left = randint(2*difficulty, 20*difficulty-1)
    right = randint(1, left)

    if (randint(1, 5) > 5 - difficulty):
        left = left * 10
        right = right * 10

    return (str(left) + ' - ' + str(right) + ' = ', left - right)

def generateMultipleEquation():
    left = randint(2*difficulty, 10*difficulty)
    if (randint(1, 5) > 5 - difficulty):
        left = left * 10

    right = randint(1, 2*difficulty)
    if (randint(1, 5) > 5 - difficulty):
        right = right * 10
    
    return (str(left) + ' * ' + str(right) + ' = ', left * right)

def generateDevideEquation():
    left = randint(1, 20*difficulty)
    right = randint(1, 2*difficulty)
    if (randint(1, 5) > 5 - difficulty):
        right = right * 10
    left = left * right
    return (str(left) + ' / ' + str(right) + ' = ', left / right)

def generateEquations(count):
    equations = []
    while count > 0:
        count = count - 1
        operatorIdx = randint(0, 3)
        if operators[operatorIdx] == '+':
            equation = generateAddEquation()
        elif operators[operatorIdx] == '-':
            equation = generateMinusEquation()
        elif operators[operatorIdx] == '*':
            equation = generateMultipleEquation()
        else:
            equation = generateDevideEquation()
        equations.append(equation)
        # print(equation)
    return equations

def DoTheMath(equations, logFile):
    unsolvedEquations = []
    while len(equations) > 0:
        count = 1
        checkpointTime = time.perf_counter()
        for equation in equations:
            print(f'{count}.')
            answer = getAnIntInput(f'\t{equation[0]}')
            if answer != equation[1]:
                unsolvedEquations.append(equation)
                logFile.write(f'{equation[0]}{answer}\tNO\n')
            else:
                logFile.write(f'{equation[0]}{answer}\tYES\n')
            count = count + 1

        timeSpend = int(time.perf_counter() - checkpointTime)
        logMsg = f'\n?????? {int(timeSpend/60)} ??? {timeSpend%60} ???, ?????????: {len(equations) - len(unsolvedEquations)} / {len(equations)}\n'
        print(logMsg)
        
        if len(unsolvedEquations) > 0:
            logMsg = f'??????????????????????????? {len(unsolvedEquations)} ???, ??????!\n'
            print(logMsg)
            logFile.write(logMsg)
        
        equations = unsolvedEquations
        unsolvedEquations = []

def getAnIntInput(msg):
    while True:
        try:
            return int(input(msg))
        except:
            pass

totalTimeSpend = 0
totalQuestions = 0
while True:
    questionCount = getAnIntInput("?????????????????????:")

    difficulty = 0
    while difficulty < 1 or difficulty > 5:
        difficulty = getAnIntInput("??????????????? (1-5): ")
    
    print(f'???????????? {questionCount} ???')
    time.sleep(1)
    countDown = 3
    while countDown > 0:
        print(f'{countDown}')
        countDown = countDown - 1
        time.sleep(1)
    print("??????!")

    Path('????????????').mkdir(exist_ok=True)
    logFile = open('????????????/' + time.strftime("%Y-%m-%d") + '.log', 'a')
    logFile.write(f'\n{"*"*50}\n\n?????? {questionCount} ???, ?????? {difficulty}\n')

    print('-'*50)
    time.sleep(1)
    equations = generateEquations(questionCount)
    startTime = time.perf_counter()
    DoTheMath(equations, logFile)
    print('-'*50)

    timeSpend = int(time.perf_counter() - startTime)
    totalTimeSpend += timeSpend
    totalQuestions += questionCount
    logMsg = f'\n?????????! ?????? {questionCount} ?????????! ????????? {int(timeSpend/60)} ??? {timeSpend%60} ???\n'
    print(logMsg)
    logFile.write(logMsg)
    time.sleep(2)

    retry = getAnIntInput(f'\n?????????????????????1, ?????????????????????:')
    if retry != 1:
        logFile.write(f'\n{"#"*80}\n???????????? {totalQuestions} ???, ?????? {int(totalTimeSpend/60)} ??? {totalTimeSpend%60} ???')
        logFile.close()
        break