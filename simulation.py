import random

##Knockout
probabilities=[[0,0.54,0.56,0.58,0.6,0.65,0.7,0.75],[0.46,0,0.54,0.56,0.58,0.6,0.65,0.7],[0.44,0.46,0,0.54,0.56,0.58,0.6,0.65],[0.42,0.44,0.46,0,0.54,0.56,0.58,0.6],[0.4,0.42,0.44,0.46,0,0.54,0.56,0.58],[0.35,0.4,0.42,0.44,0.46,0,0.54,0.56],[0.3,0.35,0.4,0.42,0.44,0.46,0,0.54],[0.25,0.3,0.35,0.4,0.42,0.44,0.46,0]]
#This is the table of probabilities of each team beating each other team
outcome = [0,0,0,0,0,0,0,0]
#This is the list to store number of wins per team
loopnum = 1000000
for z in range(0,loopnum):
    currdraw = [[0,7],[3,4],[1,6],[2,5]]
    #This is the layout for an ideal knockout tournament
    for i in range(0,4):
        win = []
        for a in range(0,len(currdraw)):
            test = random.random()
            #This sets test to a random float between 0 and 1
            if(test<probabilities[currdraw[a][0]][currdraw[a][1]]):
                win.append(currdraw[a][0])
                #If the random float is less than the probability of the given team winning, give them a win
            else:
                win.append(currdraw[a][1])
                #Otherwise give the other team a win
        currdraw = []
        if len(win)!=1:
            for i in range(0,len(win)//2):
                currdraw.append([win[(2*i)],win[(2*i)+1]])
                #This initialises the next bracket of the tournament
        else:
            outcome[win[0]]+=1
            #This add the win to the outcome list
for i in range(0,len(outcome)):
    outcome[i]/=loopnum
    #This finds the probability from the number of wins
print(outcome)

##ROUND ROBIN
wins2 = [0,0,0,0,0,0,0,0]
for i in range(0,loopnum):
    wins = [0,0,0,0,0,0,0,0]
    loopnum1 = 0
    #This variable ensures every result is only recorded once
    for a in range(0,len(probabilities)):
                   for b in range(loopnum1,len(probabilities[a])):
                       if(probabilities[a][b]>random.random()):
                           wins[a]+=1
                           #If the random float is less than the probability of the given team winning, give them a win

                       else:
                           wins[b]+=1
                           #Otherwise give the other team a win
                   loopnum1+=1
    wins2[wins.index(max(wins))]+=1
    #This adds the team with the most wins in the round robin to the total counter
for i in range(0,len(wins2)):
    wins2[i]/=loopnum
    #This finds the probability from the number of wins
print(wins2)
