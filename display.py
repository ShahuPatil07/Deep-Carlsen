import pygame
from board import Board
from square import *



class Game:
    def __init__(self):
        self.board= Board()
        self.dragger= Dragger()
        self.piece= self.dragger.piece
        self.next_player='white'

        pass
    def bg(self, bg):
        for row in range(8):
            for col in range(8):
                if (row+col)%2==0:
                    color= (102, 51, 153)
                else:
                    color=  (216, 191, 216)    
                rect= (col*100, row*100, 100, 100)
                pygame.draw.rect(bg, color, rect)

    def add_pieces(self, surface):
        for row in range(8):
            for col in range(8):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                  
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * 100 + 100 // 2, row * 100 + 100 // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
       

        if self.dragger.dragging:
            piece = self.dragger.piece

            # loop all valid moves
            for move in piece.moves:
                
                if (move.final.row+move.final.col)%2==1:
                    color = (255,165,0)
                else:
                    color= (200,100,0)     
               
                rect = (move.final.col * 100, move.final.row * 100, 100, 100)
                
                pygame.draw.rect(surface, color, rect)
    def next_turn(self):
        if self.next_player=='white':
            self.next_player='black'
        else:
            self.next_player='white'                    
