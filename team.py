class Team:

    def __init__(self):
        self.players = []
        self.out = []
        self.left = ()
        self.playing = []

    def add_player(self, player):
        self.players.append(player)
        self.left = list(self.players)

    def get_batsman_on_strike(self):
        return self.playing[0]

    def play_ball(self, ball):
        pass
