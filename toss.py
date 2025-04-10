import random
toss = int(input('How many times do you wish to toss the coin:'))
heads = 0
tails = 0
toss_num = random.randint(1,2)
while toss > 0:
    if toss_num == 1:
        heads += 1
        toss -= 1
    else:
        tails += 1
        toss -= 1
print('Heads:',heads,'\n tails:',tails)