from batsman import Batsman
team_1 = []
team_2 = []
no_of_players = int(input("No. of players for each team:"))
no_of_overs = int(input("No. of overs:"))
sides_to_play = 2
while(sides_to_play):
    print("Batting Order for team " + str(3 - sides_to_play))
    for i in range(no_of_players):
        team_1.append(Batsman(input("")))
    overs_left = no_of_overs
    while(overs_left):
        print("Over " + str(no_of_overs - overs_left + 1))
        balls_left = 6
        while(balls_left):
            input("")
            balls_left -= 1
        overs_left -= 1
    sides_to_play -= 1
