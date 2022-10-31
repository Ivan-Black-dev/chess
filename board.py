from pieces import *

class Board:

    boardList = []

    def __init__(this):
        this.boardList = [  [' ' for j in range(0, 8)]  for i in range(0, 8) ]


    def __str__ (this):
        res = ''
        b = this.boardList
        for y in b:
            res += '|'
            for x in y:
                res += f'{str(x)} |'
            res += '\n'
        return res

    
    def step():
        pass


if __name__ == '__main__':
    b = Board()
    b.boardList[0][0] = Queen(True)
    print(b)