from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares= [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COL)]
        self.create()
        self.put_peices("white")
        self.put_peices("black")
    def create(self):
        for row in range(ROW):
            for col in range(COL):
                self.squares[row][col]= Square(row,col)
                
    def put_peices(self, color):
        pawn_row,majorpiece_row=1,0
        if color=='white': 
            pawn_row, majorpiece_row= 6,7
        
        for col in range(COL):
            self.squares[pawn_row][col]= Square(pawn_row, col, Pawn(color))

        self.squares[majorpiece_row][0]= Square(majorpiece_row,0, Rook(color))
        self.squares[majorpiece_row][1]= Square(majorpiece_row,1, Knight(color))
        self.squares[majorpiece_row][2]= Square(majorpiece_row,2, Bishop(color))
        self.squares[majorpiece_row][3]= Square(majorpiece_row,3, Queen(color))
        self.squares[majorpiece_row][4]= Square(majorpiece_row,4, King(color))
        self.squares[majorpiece_row][5]= Square(majorpiece_row,5, Bishop(color))
        self.squares[majorpiece_row][6]= Square(majorpiece_row,6, Knight(color))
        self.squares[majorpiece_row][7]= Square(majorpiece_row,7, Rook(color))        


    def possible_moves(self,piece,row,col):
        pass
        if isinstance(piece, Pawn):
            pass
        if isinstance(piece, Knight):
            pass
        if isinstance(piece, Bishop):
            pass
        if isinstance(piece, King):
            pass
        if isinstance(piece, Queen):
            pass
        if isinstance(piece, Rook):
            pass
