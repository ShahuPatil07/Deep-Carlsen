class Move:
    def __init__(self,initial,final):
        self.initial=initial
        self.final=final
    def __eq__(self,move2):
        if self.initial==move2.initial and self.final==move2.final:
            return True
        return False
