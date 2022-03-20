import random


#State Initialization of the game
no_of_players = int(input('Enter the number of player : '))
max_Score = int(input('Enter max score : '))
score_table = [0] * no_of_players
prev_score = [0]*no_of_players
list_of_player = [x+1 for x in range(len(score_table))]
stack =[]
round =0

#fuction to check the end of the game
def play_end(score_table):
    if(len(stack) >= len(score_table)):
        return False
    else:
        return True

#function to reward player who scored 6 
def score_six(player,score_table):
    print('Player',player+1,"scores 6 will go again")
    dice_res = random.randint(1,6)
    print("After 6, Dice Output : ",dice_res)
    if(score_table[player]+dice_res < max_Score):
        score_table[player]+=dice_res
    else:
        score_table[player] = max_Score
   
    if(dice_res == 6) and (score_table[player] < max_Score):
        score_six(player,score_table)
    elif (score_table[player] == max_Score):
        stack.append(player+1)
        list_of_player.remove(player+1)
        print("Player %d finished"%(i+1))
        return
    else:
        if(dice_res == 1):
            prev_score[player] = dice_res
        return


#Gameplay Loop
while(play_end(score_table)):
    round+=1
    print("*********************__ Round %d __*********************"%(round))
    for i in range(no_of_players):
        if(prev_score[i] != 2):
            if(i+1 not in stack):
                print("Player-%d its your turn"%(i+1))
                dice_res = random.randint(1,6)
                print("Dice result : ",dice_res) 
                if(score_table[i]+dice_res < max_Score):
                    score_table[i] +=dice_res 
                else:
                    score_table[i] = max_Score
                #new if
                if(score_table[i] < max_Score):
                    if(dice_res == 6 ):
                        prev_score[i]=0
                        score_six(i,score_table)
                    elif(dice_res == 1) and (prev_score[i] != 1):
                        prev_score[i]=dice_res
                    elif dice_res == 1 and prev_score[i] == 1 :
                        prev_score[i]=2
                    elif dice_res != 1 and prev_score != 0:
                        prev_score[i]=0
                else:
                    if( i+1 not in stack):
                        stack.append(i+1)
                        list_of_player.remove(i+1)
                        print("Player %d finished"%(i+1))
                    if(len(list_of_player) == 1):
                        stack.append(list_of_player[0])
                        list_of_player.pop(0)
                    
        else:
            prev_score[i] = 0
            print("Player-%d your have a penalty, Round skipped"%(i+1))
    rank = [[x,i] for i,x in enumerate(score_table)]
    rank.sort(reverse=True)
    print("Player Rankings after round %d"%(round))
    for i in range(len(rank)):
        print("Player %d  score : %d"%(rank[i][1] +1 ,rank[i][0]))

    
#Ranking
print("*********************__Game Finished__*********************")        
print("Player rankings are")
for i in stack:
    print("Player ",i,"\n")

        
