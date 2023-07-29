import os
import pygame


class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []

class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)
    def fen_symbol(self):
        return 'P' if self.color == 'white' else 'p'    

class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)
    def fen_symbol(self):
        return 'N' if self.color == 'white' else 'n'     

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)
    def fen_symbol(self):
        return 'B' if self.color == 'white' else 'b'     

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)
    def fen_symbol(self):
        return 'R' if self.color == 'white' else 'r'     

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)
    def fen_symbol(self):
        return 'Q' if self.color == 'white' else 'q'     

class King(Piece):

    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 10000.0)
    def fen_symbol(self):
        return 'K' if self.color == 'white' else 'k'  
class Move:
    def __init__(self,initial,final):
        self.initial=initial
        self.final=final
        self.is_capture= False
        if final.has_piece():
            self.is_capture= True
    def __eq__(self,move2):
        if self.initial==move2.initial and self.final==move2.final:
            return True
        return False
class Square:
    def __init__(self,row,col,piece=None):
        self.row=row
        self.col=col
        self.piece=piece
    def __eq__(self,square2):
        if self.row==square2.row and self.col==square2.col:
            return True
        return False
    def has_piece(self):
        if self.piece!=None:
            return self.piece
        return None 
    def is_empty(self):
        if self.has_piece():
            return False
        return True
    def has_team_piece(self, color):
        if self.has_piece() and self.piece.color == color:
            return True
        return False
    

    def has_rival_piece(self, color):
        if self.has_piece() and self.piece.color != color:
            return True
        return False
    def is_empty_or_has_rival_piece(self,color):
        if self.is_empty() or self.has_rival_piece(color):
            return True
        else:
            return False

    @staticmethod
    def on_board(*args):
        for arg in args:
            if arg<0 or arg>7:
                return False
        return True  


class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.initial_row = 0
        self.initial_col = 0

    

    def update_blit(self, surface):
       
        self.piece.set_texture(size=80)
        texture = self.piece.texture
       
        img = pygame.image.load(texture)
        img_center = (self.mouse_x, self.mouse_y)
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)

    

    def update_pos(self, pos):
        self.mouse_x, self.mouse_y = pos 

    def save_initial_pos(self, pos):
        self.initial_row = pos[1] // 100
        self.initial_col = pos[0] // 100

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False


        

