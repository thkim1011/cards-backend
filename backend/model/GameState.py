import random
import string

class GameState: 
    def __init__(self, game_type, num_players):
        self.game_type = game_type
        self.game_id = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
        self.players = []
        self.spectators = []
        self.messages = []
        self.num_players = num_players

    def set_owner(self, username):
        self.owner = username