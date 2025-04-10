#3b
num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))
i = 1
while (i <= num1)and(i<=num2):
    if (num1 % i == 0) and (num2 % i == 0):
        div = i
    i += 1
print('GCD:',div)