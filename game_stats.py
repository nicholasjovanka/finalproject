
class Gamestats:
    def __init__(self,settings):
        self.game_active=False
        self.settings=settings
        self.score=0
        self.high_score=0
        self.level=1
        self.load_data()

    def load_data(self):#To load the highscore data
        with open("highscore.txt") as f:
            try:
                self.high_score=int(f.read())
            except:
                self.high_score=0



