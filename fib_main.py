def Fibonacci(m):
    num1 = 0
    num2 = 1
    numbers = [0,1]
    while num2 <= m:
        temp = num2
        num2 += num1
        num1 = temp
        numbers.append(num2)  
    return numbers

def c_fun(x):
    nums = []
    while x > 1:
        nums.append(x)
        if x % 2 == 0:
            x = x / 2
        else:
            x = (3 * x) + 1
    return nums

def is_fibonacci_number(n):
    num1 = 0
    num2 = 1
    flag = False
    while num2 <= n:
        if n == num2 or n == num1:
            flag = True
        temp = num2
        num2 += num1
        num1 = num2
    return flag

print('Hello, and welcome to this lovely program!!')
while True:
    user = input('Please pick a program you would like to use(1.Fibonacci,2.Triangular number sequence,3.Callatz sequence,4.Quit)')
    if user == '1' or user == 'Fibonacci':
    
        #what fibonacci is greater
        nums = Fibonacci(int(input('Enter a number:')))
        print(nums[len(nums) - 1], 'is greater fibonacci')
        nums.pop()
        print(nums)
        
        #2
        
        number = int(input('Enter a number to test if Fibonacci:'))
        if is_fibonacci_number(number):
            print('This is a fibonacci number')
        else:
            print('This is not a fibonacci number')
            
    elif user == '2' or user == 'Triangular number sequence':
        user_num = int(input('Enter the number of triangles in sequence:'))
        counter = 0
        for rows in range(1,user_num + 1):
            for cols in range(rows):
                counter += 1
            print(counter,end = ' ')
    elif user == '3' or user == 'Callatz sequence':
        num = int(input('Enter a number:'))
        print('Callatz(',num,'):',c_fun(num))   
    elif user == '4' or user == 'Quit':
        break