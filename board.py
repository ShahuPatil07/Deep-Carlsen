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
        def king_moves():
            all_moves=[
                (row-1,col),
                (row-1,col+1),
                (row-1,col-1),
                (row+1,col),
                (row+1,col-1),
                (row+1,col+1),
                (row,col-1),
                (row,col+1)]
            for moves in all_moves:
                moved_row,moved_col=moves
                if Square.on_board(moved_row,moved_row):
                    if self.squares[moved_row][moved_col].is_empty_or_has_rival_piece(piece.color):
                       intial= Square(row,col)
                       final= Square(moved_row,moved_col)
                       move= Move(intial,final)
                       piece.add_move(move)

        def pawn_moves():
            steps=2
            if piece.moved:
                steps=1
            
            start= row+piece.dir
            end= row+ piece.dir*(1+steps)
            for move_row in range(start, end, piece.dir):
                if Square.on_board(move_row,col):
                    if self.squares[move_row][col].is_empty():
                       intial=Square(row,col)
                       final=Square(move_row,col)
                       move=Move(intial,final)
                       piece.add_move(move)
                    else:
                       break
                
            if Square.on_board(start,col-1):
                if self.squares[start][col-1].has_rival_piece(piece.color):
                    intial=Square(row,col)
                    final=Square(start,col-1)
                    move=Move(intial,final)
                    piece.add_move(move)
            if Square.on_board(start,col+1):
                if self.squares[start][col+1].has_rival_piece(piece.color):
                    intial=Square(row,col)
                    final=Square(start,col+1)
                    move=Move(intial,final)
                    piece.add_move(move)        

        def knight_moves():
            all_moves=[
                (row-1,col-2),
                (row-1,col+2),
                (row-2,col+1),
                (row-2,col-1),
                (row+1,col+2),
                (row+1,col-2),
                (row+2,col+1),
                (row+2,col-1)
            ]
            for move in all_moves:
                crr_row,crr_col=move
                if Square.on_board(crr_row,crr_col):
                    if self.squares[crr_row][crr_col].is_empty_or_has_rival_piece(piece.color):
                        ini= Square(row,col)
                        fin= Square(crr_row,crr_col)
                        move= Move(ini,fin)
                        piece.add_move(move)
        def common_algo_moves(incs):
            for inc in incs:
                inc_row,inc_col=inc
                moved_row=row+inc_row
                moved_col=col+inc_col
                while True:
                    
                    intial= Square(row,col)
                    final=Square(moved_row,moved_col)
                    move= Move(intial,final)
                             
                    if Square.on_board(moved_row,moved_col):
                        if self.squares[moved_row][moved_col].is_empty():
                            piece.add_move(move)
                            
                        if self.squares[moved_row][moved_col].has_rival_piece(piece.color):
                            piece.add_move(move)  
                            break
                        if self.squares[moved_row][moved_col].has_team_piece(piece.color):
                            break
                    else:
                        break   
                    moved_row=moved_row+inc_row
                    moved_col=moved_col+inc_col

                            
        if isinstance(piece, Pawn):
            pawn_moves()
        if isinstance(piece, Knight):
            knight_moves()
        if isinstance(piece, Bishop):
            common_algo_moves([
                (-1,1),
                (-1,-1),
                (1,1),
                (1,-1)
            ])
        if isinstance(piece, King):
            king_moves()
        if isinstance(piece, Queen):
            common_algo_moves([
                (-1,1),
                (-1,-1),
                (1,1),
                (1,-1),
                (-1,0),
                (1,0),
                (0,1),
                (0,-1)
            ])
        if isinstance(piece, Rook):
            common_algo_moves([
                (-1,0),
                (1,0),
                (0,1),
                (0,-1)
            ])
    def move(self,piece,move):
        piece.moved=True
        initial=move.initial
        final=move.final
        initial_row=initial.row
        initial_col=initial.col
        final_row=final.row
        final_col=final.col

        self.squares[initial_row][initial_col].piece= None
        self.squares[final_row][final_col].piece=piece
        piece.clear_moves()
    def is_valid_(self,piece,move):
        if move in piece.moves:
            return True
        return False    
