
class Square:
    def __init__(self,row,col,piece=None):
        self.row=row
        self.col=col
        self.piece=piece
    def has_piece(self):
        if self.piece!=None:
            return self.piece
        else:
            return None 
    def is_empty(self):
        if self.has_piece():
            return False
        else:
            return True
    def has_team_piece(self,color):
        if self.piece.color== color:
            return True
        else:
            return False
    def has_rival_piece(self,color):
        if self.piece.color!= color:
            return True
        else:
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


        
