# # Variables 
# # hero = 55.98
# # # You cannot use special Characters
# # # you cannot use your first character as a number 
# # # instead of Spaces you can use Underscores
# # name_of_the_boy = "Sri"
# # bol = True
# # opp_bol = False
# # # print(hero)



# # age = 24


# # print(age)
# # print(type(age))
# # # Data Types : int, float ,string , boolean,complex,
# # # Data Strucutres of python: List, Dict, set , tuple, frozenset.


# # print(age,name_of_the_boy,sep="\n")
# # #now use variables of age phone number and your name along with their types shown stpe by step






# # # Arthemeatic operators +, -, *, /, //, %, **
# print(5%3)
# print(7%5)

# print(2**3)
# print(22/7)
# # Area of circle -pi r square
# pi = 3.143
# r = 1
# area = pi*(r**2)
# print("area of Circle: ",area)



# I wanted to find whether a number from user is an odd number or an Even number.

# num = int(input("Enter a number: "))

# # remainder = num%2
# if  num%2== 0:
#     print("Even")
# else:
#     print("odd")

# Find out whether a number is Divisible by 5 or not take the input from User.
#Number divisible by both 5 and 10 are not

# two numbers from user and an arthmetic symbol from user +,-,*,/ : msg check your symbol properly
# apply thAt operation entered by user to the two input numbers
# num1 = int(input("Enter the Number 1: "))
# num2 = int(input("Enter the number 2: "))


# Operator = input("Enter the Arthemtic operator(+,-,*,/,**): ")


# if Operator == "+":
#     print(num1+num2)

# elif Operator == "-":
#     print(num1-num2)

# elif Operator == "*":
#     print(num1*num2)

# elif Operator == "/":
#     if num2 == 0:
#         print("num2 cannot be zer0")
#     else:
#         print(num1/num2)
# else:
#     print("Error Msg: Enter the Correct Arthmetic Operator")

# Total Expenses and you know about User salary(in dollars)
# Find Out his savings 

# if the user savings are more than $500, You are stable with your savings keep going
# if the savings are less than 500$ , You should consider saving more money


# Determine how many numbers between 1 and 100 are divisible by both 3 and 5.
#15,30,45,60,75 num%15
#num%3==0 and num%5==0
# count = 0
# for num in range(1,101):
#     if num%3==0 and num%5==0 :
#         count  = count+1
# print(count)

# Determine what is the sum of all the  odd numbers from 1 to 50.
# add = 0
# for num in range(1,51):
#     add += num
# print(add)




#Calculate the factorial of a number. 
#The factorial of a number n is the product of 
#all positive integers less than or equal to n.


# n = 5
# ans = 1
# if n == 0:
#     print(1)
# for i in range(1,n+1):
#     ans = ans*i # ans *= i
# print(ans)






# # SImple Calculator
# # Objective: Build a simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.
# # Features:
# # Prompt the user to enter two numbers.
# # Ask the user to choose an operation (+, -, *, /).
# # Perform the operation and display the result.
# # Handle basic error conditions, such as division by zero.






import functions as ft

ans = ft.op_factorials([3,4,5])
print(ans)
