"""
Program: ComputeArea

Author: Rosanne Els
Student Number: 012345678

Input:none

Output:Area of a circle with radius 20

"""
import math,random

# Assign a radius
radius = float(input('Enter a radius:')) # radius is retrieved from user

# Compute area
area = radius * radius * math.pi

# Display results
print("The area for the circle of radius", radius, "is", area)

#1.2
#Assign radius
rad = float(input('Enter a radius:'))
length = float(input('Enter a height:'))

#Calculation
volumeC = math.pow(rad,2) * math.pi * length

# Display result
print("The volume of the cylinder of radius", rad, "is",volumeC)

#2
initial = float(input('Enter the initial velocity:'))
acc = float(input('Enter the acceleration:'))
time = float(input('Enter the time taken:'))

#calculate
velocity = initial + (acc * time)
#display
print('The final velocity is',velocity,'m/s')

#3
pound = float(input('Enter the pounds:'))
#calc
kilo = pound * 0.454
#display
print('The weight of',pound, 'pounds is',kilo,'kilos')


#4
P = float(input('Enter the principle amount:'))
N = float(input('Enter the years:'))
r = float(input('Enter the interest rate:')) / 100
#calc
A = (P * math.pow(1 + r,N) * r)/(math.pow(1 + r,n) - 1)
#display result
print('The accumulated amount is',A,'rands')
