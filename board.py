from const import *
from square import Square
from piece import *
from move import Move
import copy

class Board:
    def __init__(self):
        self.squares= [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COL)]
        self.create()
        self.put_peices("white")
        self.put_peices("black")
        self.move_is_castle=False
        
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
    def check_promotion(self,piece,final):
        if final.row==0 or final.row==7:
            self.squares[final.row][final.col].piece=Queen(piece.color)    
    def in_check(self, piece, move):
        in_check = False
        test_piece = copy.deepcopy(piece)
        test_board = copy.deepcopy(self)
        test_board.move(test_piece, move)
        for row in range(ROW):
            for col in range(COL):
                if test_board.squares[row][col].has_rival_piece(test_piece.color):
                    piece2 = test_board.squares[row][col].piece
                    test_board.possible_moves(piece2, row, col, bool=False)
                    for move2 in piece2.moves:
                        if isinstance(move2.final.piece, King):
                            in_check = True
                            break
                if in_check:
                    break
            if in_check:
                break

        return in_check
    


        
        
        
       


    def possible_moves(self,piece,row,col,bool=True):
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
                if Square.on_board(moved_row,moved_col):
                    if self.squares[moved_row][moved_col].is_empty_or_has_rival_piece(piece.color):
                       intial= Square(row,col)
                       final= Square(moved_row,moved_col)
                       move= Move(intial,final)
                       if bool:
                           if not self.in_check(piece,move):
                              piece.add_move(move)
                       else:
                           piece.add_move(move)
           ##short castle
            if not piece.moved:
                if piece.color=='white':
                    if self.squares[7][5].is_empty() and self.squares[7][6].is_empty(): 
                        if  self.squares[7][7].has_piece():
                           if not self.squares[7][7].piece.moved:
                               intial= Square(7,4)
                               final= Square(7,6)
                               move= Move(intial,final)
                               if bool:
                                  if not self.in_check(piece,move):
                                            piece.add_move(move)
                               else:
                                        piece.add_move(move)
                               ini= Square(7,7)
                               fin= Square(7,5)
                               move2= Move(ini,fin)
                               if bool:
                                   if not self.in_check(piece,move):
                                      self.squares[7][7].piece.add_move(move2)
                               else:
                                   self.squares[7][7].piece.add_move(move2)
                                          
                if piece.color=='black':
                    if self.squares[0][5].is_empty() and self.squares[0][6].is_empty(): 
                        if  self.squares[0][7].has_piece():
                           if not self.squares[0][7].piece.moved:
                               intial= Square(0,4)
                               final= Square(0,6)
                               move= Move(intial,final)
                               if bool:
                                   if not self.in_check(piece,move):
                                       piece.add_move(move)
                               else:
                                   piece.add_move(move)        
                               ini= Square(0,7)
                               fin= Square(0,5)
                               move2= Move(ini,fin)
                               if bool:
                                   if not self.in_check(piece,move):
                                      self.squares[0][7].piece.add_move(move2)
                               else:
                                   self.squares[0][7].piece.add_move(move2)                               
                           
                 
            ##long castle:
            if not piece.moved:
                if piece.color=='white':
                    if self.squares[7][3].is_empty() and self.squares[7][2].is_empty():
                        if self.squares[7][1].is_empty(): 
                            if self.squares[7][0].has_piece():
                               if not self.squares[7][0].piece.moved:
                                  intial= Square(7,4)
                                  final= Square(7,2)
                                  move= Move(intial,final)
                                  if bool:
                                     if not self.in_check(piece,move):
                                         piece.add_move(move)
                                  else:
                                      piece.add_move(move)
                                  ini= Square(7,0)
                                  fin= Square(7,3)
                                  move2= Move(ini,fin)
                                  if bool:
                                      if not self.in_check(piece,move):
                                          self.squares[7][0].piece.add_move(move2)
                                  else:
                                      self.squares[7][0].piece.add_move(move2)
                                      
                if piece.color=='black':
                    if self.squares[0][3].is_empty() and self.squares[0][2].is_empty():
                        if self.squares[0][1].is_empty():
                            if self.squares[0][0].has_piece(): 
                               if not self.squares[0][0].piece.moved:
                                  intial= Square(0,4)
                                  final= Square(0,2)
                                  move= Move(intial,final)
                                  piece.add_move(move)
                                  ini= Square(0,0)
                                  fin= Square(0,3)
                                  move2= Move(ini,fin)
                                  if bool:
                                      if not self.in_check(piece,move):
                                          self.squares[0][0].piece.add_move(move2)
                                  else:
                                      self.squares[0][0].piece.add_move(move2)
                                      
                                                


                          

            


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
                       if bool:
                           if not self.in_check(piece,move):
                              piece.add_move(move)
                       else:
                           piece.add_move(move) 
                                 
                    else:
                       break
                else:
                    break

            if Square.on_board(start,col-1):
                if self.squares[start][col-1].has_rival_piece(piece.color):
                    intial=Square(row,col)
                    final_piece=self.squares[start][col-1].piece
                    final=Square(start,col-1,final_piece)
                    move=Move(intial,final)
                    if bool:
                           if not self.in_check(piece,move):
                              piece.add_move(move)
                    else:
                           piece.add_move(move) 
            if Square.on_board(start,col+1):
                if self.squares[start][col+1].has_rival_piece(piece.color):
                    intial=Square(row,col)
                    final_piece=self.squares[start][col+1].piece
                    final=Square(start,col+1,final_piece)
                    move=Move(intial,final)
                    if bool:
                           if not self.in_check(piece,move):
                              piece.add_move(move)
                    else:
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
                        final_piece=self.squares[crr_row][crr_col].piece
                        fin= Square(crr_row,crr_col,final_piece)
                        move= Move(ini,fin)
                        if bool:
                           if not self.in_check(piece,move):
                              piece.add_move(move)
                        else:
                           piece.add_move(move)
                           break
        def common_algo_moves(incs):
            for inc in incs:
                inc_row,inc_col=inc
                moved_row=row+inc_row
                moved_col=col+inc_col
                while True:
                    
                    
                    
                             
                    if Square.on_board(moved_row,moved_col):
                        if self.squares[moved_row][moved_col].is_empty():
                            intial= Square(row,col)
                            final_piece=self.squares[moved_row][moved_col].piece
                            final=Square(moved_row,moved_col,final_piece)
                            move= Move(intial,final)
                            if bool:
                                if not self.in_check(piece,move):
                                     piece.add_move(move)
                            else:
                                 piece.add_move(move)
                            
                            
                        elif self.squares[moved_row][moved_col].has_rival_piece(piece.color):
                            intial= Square(row,col)
                            final_piece=self.squares[moved_row][moved_col].piece
                            final=Square(moved_row,moved_col,final_piece)
                            move= Move(intial,final)
                            if bool:
                                if not self.in_check(piece,move):
                                    piece.add_move(move)
                            else:
                                 piece.add_move(move) 
                            
                            break
                        elif self.squares[moved_row][moved_col].has_team_piece(piece.color):
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
        if isinstance(piece,King):
            if final.col-initial.col>1 or initial_col-final.col>1:
                if piece.color=='white':
                    if final.col==6:
                       
                       self.squares[7][5].piece=self.squares[7][7].piece
                       self.squares[7][7].piece=None
                       self.squares[7][5].piece.clear_moves()
                    if final.col==2:
                       
                       self.squares[7][3].piece=self.squares[7][0].piece 
                       self.squares[7][0].piece=None
                       self.squares[7][3].piece.clear_moves()
                if piece.color=='black':
                    if final.col==6:
                       
                       self.squares[0][5].piece=self.squares[0][7].piece
                       self.squares[0][7].piece=None
                       self.squares[0][5].piece.clear_moves()
                    if final.col==2:
                       
                       self.squares[0][3].piece=self.squares[0][0].piece
                       self.squares[0][0].piece=None
                       self.squares[0][3].piece.clear_moves()          
    
        

        if isinstance(piece,Pawn):
            self.check_promotion(piece,final)
    def is_valid_(self,piece,move):
        if move in piece.moves:
            return True
        return False    
