import random
import string

class GameState: 
    def __init__(self, gameType):
        self.gameType = gameType
        self.gameId = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
        self.players = []