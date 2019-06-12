"""
Python Program to Determine Whether a Given Number is Even or Odd Recursively
"""

# def recEvenOdd(num):
#     if num%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# recEvenOdd(5)

def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n=int(input("Enter number:"))
if(check(n)):
      print("Number is even!")
else:
      print("Number is odd!")

# n = 2
# assert n<=2