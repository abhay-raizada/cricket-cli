from batsman import Batsman
from team import Team
from ball import Ball


def over_string(overs_left, ball_left, no_of_overs):
    print(str(overs_left) + " " + str(ball_left) + str(no_of_overs))
    if balls_left == 6:
        return str(no_of_overs - overs_left) + ".0"
    if balls_left == 0:
        return str(no_of_overs - overs_left + 1) + ".0"
    else:
        return str(no_of_overs - overs_left) + "." + str(6 - balls_left)

teams = []
no_of_players = int(input("No. of players for each team:"))
no_of_overs = int(input("No. of overs:"))
batting_team = 0
while(batting_team < 2):
    print("Batting Order for team " + str(batting_team + 1))
    players = []
    for i in range(no_of_players):
        players.append(Batsman(input("")))
    teams.append(Team(list(players)))
    overs_left = no_of_overs
    all_out = False
    reached_target = False
    remaining_balls = 0
    while(overs_left and not all_out and not reached_target):
        balls_left = 6
        print("Over " + over_string(overs_left, balls_left, no_of_overs))
        while(balls_left):
            ball = Ball(input(""))
            teams[batting_team].play_ball(ball)
            if ball.is_legal():
                balls_left -= 1
            if teams[batting_team].all_out:
                all_out = True
                remaining_balls = balls_left
                break
            if teams[batting_team].total > teams[0].total:
                reached_target = True
                remaining_balls = ball_left
                break
        teams[batting_team].scorecard(over_string(overs_left, balls_left, no_of_overs))
        if not balls_left:
            overs_left -= 1
    teams[batting_team].scorecard(over_string(overs_left, balls_left, no_of_overs))
    batting_team +=1

if teams[0].total > teams[1].total:
    print("Team 1 won the match by" + str(teams[0].total - teams[1].total) + "Runs" )
elif teams[1].total > teams[0].total:
    print("Team 2 won the match by" + str(len(team[1].batting_manager.left)) + "Wickets")
else:
    print("The Match was a tie")
