import math
num = int(input('Enter a perfect square:'))
init = math.sqrt(num)
cube = num * init
if cube > 2000:
    rating = 'large perfect cube'
elif (cube >= 500) and (cube <= 2000):
    rating = 'medium perfect cube'
else:
    rating = 'small perfect cube'
print(cube,'is a',rating)
response = input('Continue(Y/N):')
while response == 'Y':
    num = int(input('Enter a perfect square:'))
    init = math.sqrt(num)
    cube = num * init
    if cube > 2000:
        rating = 'large perfect cube'
    elif (cube >= 500) and (cube <= 2000):
        rating = 'medium perfect cube'
    else:
        rating = 'small perfect cube'
    print(cube,'is a',rating)
    response = input('Continue(Y/N):')