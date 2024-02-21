# A program to solve a quadratic equation
# Date : 15/02/2024
# Name : Austin Musango
import math

a = float(input("enter the coefficient of first term :"))
b = float(input("enter the coefficient of second term :"))
c = float(input("enter the constant :"))


d =(float(b)**2) - 4 * float(a) * float(c)

x_1 = (-b + math.sqrt(d) ) / 2* a
x_1 = (-b - math.sqrt(d) ) / 2* a

print("The solution of the quadratic equation")