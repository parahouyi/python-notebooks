from random import *


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def printIntro():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要AB的能力值（以0到1之间的小数表示')


def getInputs():
    a = eval(input('请输入选手A的能力值（0-1）：'))
    b = eval(input('请输入选手B的能力值（0-1）：'))
    n = eval(input('请输入模拟比赛的场次：'))
    return a, b, n


def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
            print(f'选手A获胜{winsA}局了')
        else:
            winsB += 1
            print(f'选手B获胜{winsB}局了')
    return winsA, winsB


def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    # global serving
    serving = 'A'
    while True:#not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA / (probA + probB):
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB / (probA + probB):
                scoreB += 1
            else:
                serving = 'A'

        return scoreA, scoreB


def gameOver(scoreA, scoreB):
    return scoreA == 15 or scoreB == 15


def printSummary(winsA, winsB):
    n = winsA + winsB
    print('竞技分析开始，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场比赛，占比{:0.1%}'.format(winsA, winsA / n))
    print('选手B获胜{}场比赛，占比{:0.1%}'.format(winsB, winsB / n))


main()
