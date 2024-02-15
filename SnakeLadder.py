import random
while True:
    player1=input("Player 1 enter your name:")
    player2=input("Player 2 enter your name:")
    player={player1:0,player2:0}
    turn=1
    fp1=0
    fp2=0
    c=0
    s={27:5,40:3,43:18,54:31,66:45,76:58,89:53,99:41}
    stair={4:25,13:46,33:49,42:63,50:69,62:81,74:92}
    print("player1",end=" ")
    while True:
        k=input("If you want to play game continue then enter y otherwise enter n:")
        if turn==1 and c==0 and (k=='y' or k=='Y'):
            turn=2
            n=random.randint(1,6)
            print("Random Number for player1= ",n)
            if fp1==0:
                player[player1]=player[player1]+n
                if player[player1] in s.keys():
                    player[player1]=s[player[player1]]
                elif player[player1] in stair.keys():
                    player[player1]=stair[player[player1]]
                elif player[player1]>100:
                    player[player1]=player[player1]-n
                elif player[player1]==100:
                    fp1=1
            else:
                player[player1]=player[player1]-n
                if player[player1] in s.keys():
                    player[player1]=s[player[player1]]
                elif player[player1] in stair.keys():
                    player[player1]=stair[player[player1]]
                elif player[player1]<1:
                    player[player1]=player[player1]+n
                elif player[player1]==1:
                    print(player1," win")
                    break
            print("player 1 position=",player[player1],"\nplayer2 position=",player[player2])
            print("player2",end=" ")
        elif turn==2 and c==0 and (k=='y' or k=='Y'):
            turn=1
            n=random.randint(1,6)
            print("Random Number for player2= ",n)
            if fp2==0:
                player[player2]=player[player2]+n
                if player[player2] in s.keys():
                    player[player2]=s[player[player2]]
                elif player[player2] in stair.keys():
                    player[player2]=stair[player[player2]]
                elif player[player2]>100:
                    player[player2]=player[player2]-n
                elif player[player2]==100:
                    fp2=1
            else:
                player[player2]=player[player2]-n
                if player[player2] in s.keys():
                    player[player2]=s[player[player2]]
                elif player[player2] in stair.keys():
                    player[player2]=stair[player[player2]]
                elif player[player2]<1:
                    player[player2]=player[player2]+n
                elif player[player2]==1:
                    print(player2," win")
                    break
            print("player 1 position=",player[player1],"\nplayer2 position=",player[player2])
            print("player1",end=" ")
        elif k=='n' or k=='N':
            break
    q=input("If tou want to play game again then press y otherwise n:")
    if q=='n' or q=='N':
        break

        
            
