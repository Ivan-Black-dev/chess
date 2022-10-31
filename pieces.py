class Piece:
    isBlack = True
    title = ''
    position = ''


    def __init__(this, isBlack, pos):
        '''
        title: 0 - пешка
               1 - лощадь
               2 - офицер
               3 - ладья
               4 - король
               5 - королева
        '''
        this.isBlack = isBlack
        this.position = pos


    def __str__(this):
        icon = {
            'pawn': {},
            'horse': {},
            'officer': {},
            'rook': {},
            'king': {},
            'queen': {}
        }
        icon = [ ['♟', '♙'], ['♞', '♘'], ['♝', '♗'], ['♜', '♖'], ['♚', '♔'], ['♛', '♕'] ]
        return icon[this.title][int(this.isBlack)]


class Queen (Piece):
    title = 5

    def canStep(this):
        x0 = this.position[0]
        y0 = this.position[1]
        canStep = []

        # Проверка диагоналей
        cL = y0 - x0
        cR = y0 + x0
        for y in range(0, 8):
            for x in range(0, 8):
                if y == (-x + cR):
                    canStep.append( (x, y) )
                if y == x + cL:
                    canStep.append( (x, y) )

        # Проверка горизональных линий
        for x in range(0, 8):
            canStep.append( (x, y0) )
        for y in range(0, 8):
            canStep.append( (x0, y) )
        return canStep

class King (Piece):
    title = 4

    def canStep(this):
        x0 = this.position[0]
        y0 = this.position[1]
        canStep = []

        # Проверка диагоналей
        cL = y0 - x0
        cR = y0 + x0
        for y in range(y0-1, y0+2):
            for x in range(x0-1, x0+2):
                if y == (-x + cR):
                    canStep.append( (x, y) )
                if y == x + cL:
                    canStep.append( (x, y) )

        # Проверка горизональных линий
        for x in range(x0-1, x0+2):
            canStep.append( (x, y0) )
        for y in range(y0-1, y0+2):
            canStep.append( (x0, y) )
        canStep = list(set(canStep))
        canStep.pop( canStep.index( (x0, y0) ) )
        return canStep


class Rook (Piece):
    title = 3


    def canStep(this):
        x0 = this.position[0]
        y0 = this.position[1]
        canStep = []

        # Проверка горизональных линий
        for x in range(0, 8):
            canStep.append( (x, y0) )
        for y in range(0, 8):
            canStep.append( (x0, y) )
        return canStep


class Officer (Piece):
    title = 2


    def canStep(this):
        x0 = this.position[0]
        y0 = this.position[1]
        canStep = []

        # Проверка диагоналей
        cL = y0 - x0
        cR = y0 + x0
        for y in range(0, 8):
            for x in range(0, 8):
                if y == (-x + cR):
                    canStep.append( (x, y) )
                if y == x + cL:
                    canStep.append( (x, y) )
        return canStep



class Horse (Piece):
    title = 1


class Pawn (Piece):
    title = 0