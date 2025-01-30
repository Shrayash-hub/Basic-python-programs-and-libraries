#write the code for building an calculator using numpy
import numpy as np

def addition(a,b):
  return np.add(a,b)

def subtraction(a,b):
  return np.subtract(a,b)

def multiplication(a,b):
  return np.multiply(a,b)

def division(a,b):
  return np.divide(a,b)

print("Welcome to my calculator\n")
n = 10
while(1):
  n = input("Enter your choice: ")
  a = int(input("Enter the value of first number: "))
  b = int(input("Enter the value of second number: "))

  if n == '0':
    print(addition(a,b))
  elif n == '1':
    print(subtraction(a,b))
  elif n == '2':
    print(multiplication(a,b))
  elif n == '3':
    print(division(a,b))
  elif n == '-1':
    print("Thank you for using my calculator")
    break
  else:
    print("Invalid input")
