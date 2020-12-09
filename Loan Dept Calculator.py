# Made by Zachary Verreault
# For Algebra 2 at Neocity Academy
# 12/2/2020 12:52 PM
import time
def add(p, r, n, t):
    return p + r + n + t

while True: 
    print("Hello! Welcome to my Loan Dept Calculator! To look at the code, you can open this\n\ndocument in a wordpad program. If you are seeing this, look around the school!\n\nThere are 5 total calculators scattered around the school! \n\n             Thank you!\n ")
    print("")
    print("")
    p = float(input("What is your Present Value? \n"))
    r = float(input("What is your intrest rate expressed as a decimal? \n"))
    t = float(input("How many years will it take to pay off your debt? \n"))
    n = float(input("How many Compound periods are present per year? \n"))    
    answer = (p * (1 + (r / n)) ** (n * t))
    print("")
    print("")
    print(answer) 
    month = answer / ((1 - (1 + (r / n)) ** (n * t)) / (1 - (1 + (r / n))))
    print(" ")
    print(" ")
    print("your monthly payment (a) is")
    print(month)
    print("")
    print("")
    print("")
    print("")
    time.sleep(2)
    