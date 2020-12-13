class Ball:

    def __init__(self, ball_string):
        self.ball_string = ball_string

    def player_runs(self):
        if self.is_byes() or self.is_leg_byes():
            return 0
        else:
            return self.extract_runs()

    def extras(self):
        extra_runs = 0
        if self.is_no_ball() or self.is_wide_ball():
            #print("NO BALL")
            extra_runs = 1
        if self.is_byes() or self.is_leg_byes():
            #print("BYEE")
            extra_runs += self.extract_runs()
        return extra_runs

    def extract_runs(self):
        if self.is_wicket():
            return 0
        else:
            try:
                extracted_runs = int(self.ball_string)
            except ValueError:
                extracted_runs = 0
        return extracted_runs

    def runs(self):
        return self.extras() + self.player_runs()

    def is_no_ball(self):
        if 'Nb' in self.ball_string:
            return True
        return False

    def is_wide_ball(self):
        if 'Wd' in self.ball_string:
            return True
        return False


    def is_wicket(self):
        if 'W' in self.ball_string and 'Wd' not in self.ball_string:
            return True
        return False

    def is_legal(self):
        if self.is_no_ball() or self.is_wide_ball():
            return False
        return True

    def is_byes(self):
        if 'B' in self.ball_string:
            return True
        return False

    def is_leg_byes(self):
        if 'LB' in self.ball_string:
            return True
        return False