num = int(input('Enter a number:'))
mult = 1
even = ''
val = True
while num > 0:
    if val:
        mult *= num % 10
    else:
        even += str(num % 10)
    val = not val
    num = num // 10
print('New num 1:',mult)
print('Nw num 2:',even)
if mult > int(even):
    print('New num 3:',mult - int(even))
else:
    print('New num 3:',int(even) - mult)