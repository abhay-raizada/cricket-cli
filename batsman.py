class Batsman:

    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.fours = 0
        self.sixes = 0
        self.balls = 0

    def play_ball(self, ball):
        self.balls += 1
        self.process_fours(ball)
        self.process_sixes(ball)
        self.add_runs(ball)

    def process_fours(self, ball):
        if ball.player_runs() == 4:
            self.fours += 1

    def process_sixes(self, ball):
        if ball.player_runs() == 6:
            self.sixes += 1

    def add_runs(self, ball):
        self.runs += ball.player_runs()