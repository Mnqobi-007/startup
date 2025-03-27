import random
rounds = int(input("How many rounds would you like to play?"))
score = 0
while rounds > 0:
    user_pick = int(input('Enter your pick [(1)-rock, (2)-paper, (3)-scissors]:'))
    comp_pick = random.randint(1,3)
    if (user_pick == 1 and comp_pick == 2):
        print('You picked rock, computer picked paper')
        print('Computer wins, paper beats rock')
    elif (user_pick == 1 and comp_pick == 3):
        print('You picked rock, computer picked scissors')
        print('You win, rock beats scissors')
        score += 1
    elif (user_pick == 2 and comp_pick == 1):
        print('You picked paper, computer picked rock')
        print('You win, paper beats rock')
        score += 1
    elif (user_pick == 2 and comp_pick == 3):
        print('You picked paper, computer picked scissors')
        print('Computer wins, scissors beats paper')
    elif (user_pick == 3 and comp_pick == 1):
        print('You picked scissors, computer picked rock')
        print('Computer wins, rock beats scissors')
    elif (user_pick == 3 and comp_pick == 2):
        print('You picked scissors, computer picked paper')
        print('You win, scissors beats paper')
        score += 1
    elif (user_pick == comp_pick):
        print("It's a draw")
    rounds -= 1
print('Score:',score,'/',rounds)
if (score / rounds)* 100 >= 50:
    print('Well done, you did well!!')