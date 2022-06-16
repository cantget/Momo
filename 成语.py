from copy import copy
from itertools import count
import random
from socket import getnameinfo

class ChengyuTest:
    def __init__(self, choices, meanning, answer) -> None:
        self.choices = {'A':str.join('', choices[0]), 'B':str.join('', choices[1]), 'C':str.join('', choices[2]), 'D':str.join('', choices[3])}
        self.answer = answer
        self.meanning = meanning
    
    def __str__(self) -> str:
        testItem = '含义: ' + self.meanning + '\n'
        for key in self.choices:
            testItem = testItem + key + '. ' + self.choices[key] + '\t'
        return testItem

with open('小学生成语200.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

ChengyuTestList = []
for line in lines:
    answer, meanning = line.strip().split('|')

    ChengYuChars = []
    for c in answer:
        ChengYuChars.append(c)
    
    choices = [ChengYuChars[:], ChengYuChars[:], ChengYuChars[:]]
    for choice in choices:
        random.shuffle(choice)
    choices.append(ChengYuChars)
    random.shuffle(choices)
    
    ChengyuTestList.append(ChengyuTest(choices.copy(), meanning, answer))
    random.shuffle(ChengyuTestList)

def GetChoice():
    choice = ''
    while choice not in ('A','B','C','D'):
        choice = input("请选择:").capitalize()
    print('\n')
    return choice

def DoTest(Tests):
    unfinishedTests = []
    while len(Tests) != 0:
        for test in Tests:
            print(test)
            choice = GetChoice()
            if (test.choices[choice] != test.answer):
                unfinishedTests.append(test)
        if len(unfinishedTests) != 0:
            print (f'* 做错了 {len(unfinishedTests)} 题呦, 加油!\n')
        Tests = unfinishedTests
        unfinishedTests = []
        
count = 0
step = 5
while True:
    print(f'\n{"-"*50}\n随机测试 {step} 个成语\n')
    DoTest(ChengyuTestList[count:count+step])
    count = count + step
    letsgo = input('挑战成功, 继续按 Y, 退出按其他键: ').capitalize()
    if (letsgo != 'Y'):
        break
