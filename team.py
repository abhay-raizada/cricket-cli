from batting_manager import BattingManager
class Team:

    def __init__(self, players):
        self.players = players
        self.batting_manager = BattingManager(list(players))
        self.total = 0
        self.extras = 0
        self.all_out = False

    def play_ball(self, ball):
        #print("Runs: " + str(ball.runs()) + "Extras: " + str(ball.extras()))
        self.total += ball.runs()
        self.extras += ball.extras()
        self.batting_manager.play_ball(ball)
        if self.batting_manager.all_out:
            self.all_out = True

    def over_end(self):
        self.batting_manager.change_strike()

    def scorecard(self, over_string):
        out, playing, left = self.batting_manager.get_stats()
        print("name\t runs) \t fours \t sixes \t balls")
        for player in out:
            self.print_player_stats(player)
        for player in playing:
            self.print_player_stats(player, playing = True)
        for player in left:
            self.print_player_stats(player)

        print("TOTAL: " + str(self.total))
        print("EXTRAS: " + str(self.extras))
        print("OVERS: " + over_string)

    def print_player_stats(self, player, playing= False):
        name = player.name
        if playing:
            name = player.name + "*"
        print(str(name)+ "\t" + str(player.runs) + "\t" + str(player.fours) + "\t" + str(player.sixes) + "\t" + str(player.balls))
