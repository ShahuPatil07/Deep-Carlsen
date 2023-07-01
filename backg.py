import pygame
from const import *
from board import Board
from square import Square
from Drag import Dragger


class Game:
    def __init__(self):
        self.board= Board()
        self.dragger= Dragger()
        self.piece= self.dragger.piece
        self.next_player='white'

        pass
    def bg(self, bg):
        for row in range(ROW):
            for col in range(COL):
                if (row+col)%2==0:
                    color= (102, 51, 153)
                else:
                    color=  (216, 191, 216)    
                rect= (col*100, row*100, 100, 100)
                pygame.draw.rect(bg, color, rect)

    def add_pieces(self, surface):
        for row in range(COL):
            for col in range(COL):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
       

        if self.dragger.dragging:
            piece = self.dragger.piece

            # loop all valid moves
            for move in piece.moves:
                # color
                color = (255,165,0) 
                # rect
                rect = (move.final.col * 100, move.final.row * 100, 100, 100)
                # blit
                pygame.draw.rect(surface, color, rect)
    def next_turn(self):
        if self.next_player=='white':
            self.next_player='black'
        else:
            self.next_player='white'                    

                rect = (move.final.col * 100, move.final.row * 100, 100, 100)
                # blit
                pygame.draw.rect(surface, color, rect)

