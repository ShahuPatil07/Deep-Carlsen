import chess
import chess.engine
import board
import piece
import move
import copy
class Stockfish_play:
    def __init__(self) :
             self.piece0= None
             
    def best_move(self,board):
       
       
       max_eval=1000.0
       for row in range(8):
           for col in range(8):
               if board.squares[row][col].has_team_piece('black'):
                   test_piece= copy.deepcopy(board.squares[row][col].piece)
                   test_board= copy.deepcopy(board)

                   test_board.possible_moves(test_piece,row,col)
                   for m in test_piece.moves:
                       test_board= copy.deepcopy(board)
                       test_board.move(test_piece,m)
                       test_board.active_color= 'white'
                       fen_position= test_board.board_to_fen()
                       
                       with chess.engine.SimpleEngine.popen_uci(r"C:\Users\shau\OneDrive\Desktop\stockfish\stockfish-windows-x86-64-avx2") as sf:
                                     crr_eval = sf.analyse(board= chess.Board(fen_position), limit=chess.engine.Limit(depth=1))\
                                     ['score'].relative.score(mate_score=10000)
                                     crr_eval=crr_eval/100
                                     if crr_eval<max_eval:
                                                max_eval= crr_eval
                                                best_move= m
                                                best_piece= test_piece
                   test_piece.clear_moves()                             
       self.piece0= best_piece   
       return best_move  
    def best_piece(self):
          return self.piece0                                   