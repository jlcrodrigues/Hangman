class Hangman:
    def __init__(self):
        self.state = 0

    def isDead(self):
        if self.state == 8:
            return True
        return False
        

    def draw(self):
        pass
