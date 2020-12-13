from batsman import Batsman
from team import Team
from ball import Ball

teams = []
no_of_players = int(input("No. of players for each team:"))
no_of_overs = int(input("No. of overs:"))
playing_team = 0
while(playing_team < 2):
    print("Batting Order for team " + str(playing_team + 1))
    players = []
    for i in range(no_of_players):
        players.append(Batsman(input("")))
    teams.append(Team(list(players)))
    overs_left = no_of_overs
    all_out = False
    reached_target = False
    over = str(no_of_overs - overs_left + 1)
    while(overs_left and not all_out and not reached_target):
        print("Over " + str(over))
        balls_left = 6
        while(balls_left):
            ball = Ball(input(""))
            teams[playing_team].play_ball(ball)
            if ball.is_legal():
                balls_left -= 1
            if teams[playing_team].all_out:
                all_out = True
                break
            if teams[playing_team].total > teams[0].total:
                reached_target = True
        teams[playing_team].scorecard(over)
        overs_left -= 1
    teams[playing_team].scorecard(over)
    playing_team +=1

if teams[0].total > teams[1].total:
    print("Team 1 won the match by" + str(teams[0].total - teams[1].total) + "Runs" )
elif teams[1].total > teams[0].total:
    print("Team 2 won the match by" + str(len(team[1].batting_manager.left)) + "Wickets")
else:
    print("The Match was a tie")
