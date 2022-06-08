from random import randint
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

def DoTheMath(equations):
    unsolvedEquations = []
    while len(equations) > 0:
        count = len(equations) - 1
        checkpointTime = time.perf_counter()
        for equation in equations:
            print(f'{len(equations) - count}.')
            count = count - 1
            answer = getAnIntInput(f'\t{equation[0]}')
            if answer != equation[1]:
                unsolvedEquations.append(equation)
        timeSpend = int(time.perf_counter() - checkpointTime)
        print(f'用时 {int(timeSpend/60)} 分 {timeSpend%60} 秒, 正确率: {len(equations) - len(unsolvedEquations)} / {len(equations)}\n')
        
        if len(unsolvedEquations) > 0:
            print(f'现在开始订正做错的 {len(unsolvedEquations)} 题, 加油!\n')
        
        equations = unsolvedEquations
        unsolvedEquations = []

def getAnIntInput(msg):
    while True:
        try:
            return int(input(msg))
        except:
            pass

while True:
    total = getAnIntInput("你要挑战多少题:")

    difficulty = 0
    while difficulty < 1 or difficulty > 5:
        difficulty = getAnIntInput("请选择难度 (1-5): ")
    
    print(f'准备挑战 {total} 题')
    time.sleep(1)
    countDown = 3
    while countDown > 0:
        print(f'{countDown}')
        countDown = countDown - 1
        time.sleep(1)
    print("开始!")

    print('-'*50)
    time.sleep(1)
    equations = generateEquations(total)
    startTime = time.perf_counter()
    DoTheMath(equations)
    print('-'*50)

    timeSpend = int(time.perf_counter() - startTime)
    print(f'太棒了! 挑战 {total} 题成功! 共用时 {int(timeSpend/60)} 分 {timeSpend%60} 秒\n')
    time.sleep(2)

    retry = getAnIntInput(f'再次挑战请输入1, 按其他数字退出:')
    if retry != 1:
        break