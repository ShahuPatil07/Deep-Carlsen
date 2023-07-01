import pygame
import sys

from const import *
from backg import Game
from square import Square
from move import Move

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):
        
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # show methods
            game.bg(screen)
            
            game.show_moves(screen)
            game.add_pieces(screen)
            

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                        dragger.update_pos(event.pos)
                   
                        clicked_row = dragger.mouse_y // SQSIZE
                        clicked_col = dragger.mouse_x // SQSIZE
                        if board.squares[clicked_row][clicked_col].has_piece():
                            piece = board.squares[clicked_row][clicked_col].piece
                            if game.next_player==piece.color:
                                board.possible_moves(piece, clicked_row, clicked_col)
                                dragger.save_initial_pos(event.pos)
                                dragger.drag_piece(piece)
                            # show methods 
                                game.bg(screen)
                            
                                game.show_moves(screen)
                                game.add_pieces(screen)
                       
                       
                            

                    
                    


                    
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    

                    if dragger.dragging:
                        dragger.update_pos(event.pos)
                        # show methods
                        game.bg(screen)
                        
                        game.show_moves(screen)
                        game.add_pieces(screen)
                    
                        dragger.update_blit(screen)
                
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_pos(event.pos)

                        released_row = dragger.mouse_y // SQSIZE
                        released_col = dragger.mouse_x // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # valid move ?
                        if board.is_valid_(dragger.piece,move):
                            board.move(dragger.piece,move)
                            self.game.bg(self.screen)
                            self.game.add_pieces(self.screen)
                            self.game.next_turn()
            

                       
                    
                    dragger.undrag_piece()
                
                # key press
                

                # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()


main = Main()
main.mainloop()
