import random

def roll():
    roll=random.randint(1,6)
    
    return roll

while True:
    players=input("enter the number of player you want only (2 or 4)!  ") 
    if players.isdigit():
        player=int(players)
        if 2 <= player <=4:
            break
        else:
            print("enter only between 2 and 4")
    else:
        print("enter the valid number ")
        
print("the number of players are ",player)

players_lst=[ 0 for _ in range(player)]
max_value=51

while max(players_lst)<max_value:
    for inx_player in range(player):
        print("its {} turn ".format(inx_player+1))
        print("total score is, ",players_lst[inx_player])
        count_points=0
        while True:
            sol=input(("DO you want to start now (y- to start ) "))
            if sol.lower()!='y':
                break
            value=roll()
            if value==1:
                print("hey you rolled one are ur out ")
                count_points=0
                break
            else:
                count_points+=value
                print("you rolled ",value)
                    
        players_lst[inx_player] += count_points
        print("ur score is "players_lst[inx_player])
        if players_lst[inx_player] >= max_value:
            print("Player {} wins!".format(inx_player + 1))
            break
            
            
        
        
        
        