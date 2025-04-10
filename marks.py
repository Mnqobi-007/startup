#3a
count = 0
sum = 0
highest = 0
mark = float(input('Enter a mark(-1 to stop):'))
lowest = mark
while mark != -1:
    count += 1
    sum += mark
    if highest < mark:
        highest = mark
    if mark < lowest:
        lowest = mark
    mark = float(input('Enter a mark(-1 to stop):'))
print('Average:',sum / count, '\nLowest:',lowest,'\nHighest:',highest)