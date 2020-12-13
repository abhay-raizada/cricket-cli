from batting_manager import BattingManager
class Team:

    def __init__(self, players):
        self.players = players
        self.batting_manager = BattingManager(list(players))
        self.total = 0
        self.extras = 0
        self.all_out = False

    def play_ball(self, ball):
        print("Runs: " + str(ball.runs()) + "Extras: " + str(ball.extras()))
        self.total += ball.runs()
        self.extras += ball.extras()
        self.batting_manager.play_ball(ball)
        if self.batting_manager.all_out:
            self.all_out = True

    def over_end(self):
        self.batting_manager.change_strike()

    def scorecard(self, overs = 0, balls = 0):
        out, playing, left = self.batting_manager.get_stats()
        print("name\t runs) \t fours \t sixes \t balls")
        for player in out:
            print(str(player.name)+ "\t" + str(player.runs) + "\t" + str(player.fours) + "\t" + str(player.sixes) + "\t" + str(player.balls))
        for player in playing:
            print(str(player.name)+ "\t" + str(player.runs) + "\t" + str(player.fours) + "\t" + str(player.sixes) + "\t" + str(player.balls))
        for player in left:
            print(str(player.name)+ "\t" + str(player.runs) + "\t" + str(player.fours) + "\t" + str(player.sixes) + "\t" + str(player.balls))

        print("TOTAL: " + str(self.total))
        print("EXTRAS: " + str(self.extras))
        print("OVERS: " + str(overs) + "." + str(balls) )
