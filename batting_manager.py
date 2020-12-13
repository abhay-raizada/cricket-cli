class BattingManager:

    def __init__(self, batsmen):
        self.batsmen = batsmen
        self.left = list(batsmen)
        player1 = self.left.pop(0)
        player2 = self.left.pop(0)
        self.playing = [player1, player2]
        self.out = []
        self.all_out = False

    def get_batsman_on_strike(self):
        return self.playing[0]

    def play_ball(self, ball):
        player_on_strike = self.get_batsman_on_strike()
        if ball.is_wicket():
           self.process_wicket(player_on_strike)
        if ball.player_runs() % 2 == 1:
            self.change_strike()
        player_on_strike.play_ball(ball)

    def change_strike(self):
        switch_player = self.playing.pop(-1)
        self.playing.insert(0, switch_player)

    def process_wicket(self, player_on_strike):
        self.out.append(player_on_strike)
        self.playing.remove(player_on_strike)
        if len(self.left):
            new_player = self.left.pop(0)
            self.playing.insert(0, new_player)
        else:
            self.all_out = True

    def get_stats(self):
        return (self.out, self. playing, self.left)