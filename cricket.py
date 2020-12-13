from batsman import Batsman
from team import Team
from ball import Ball

teams = [Team(), Team()]
no_of_players = int(input("No. of players for each team:"))
no_of_overs = int(input("No. of overs:"))
playing_team = 0
while(playing_team < 2):
    print("Batting Order for team " + str(playing_team + 1))
    for i in range(no_of_players):
        teams[playing_team].add_player(Batsman(input("")))
    overs_left = no_of_overs
    while(overs_left):
        print("Over " + str(no_of_overs - overs_left + 1))
        balls_left = 6
        while(balls_left):
            ball = Ball(input(""))
            teams[playing_team].play_ball(ball)
            if ball.is_legal():
                balls_left -= 1
        overs_left -= 1
    playing_team +=1
