# # Problem: Implement a system that allows a user up to three attempts to enter a correct password. 
# # If the user fails to enter the correct password after three attempts, 
# # the system should lock them out and display an appropriate message.
# password = "secret"
# user_input = 0
# attempt = 1
# while attempt<=3:
#     user_input = input("Enter the Password?: ")
#     if user_input == password:
#         print("Password Correct")
#         break
#     elif user_input != password and attempt!=3:
#         print("incorrect Paasword, Try again")
#     elif attempt == 3:
#         print("Too many attempts, Given Incorrect password")
#     attempt+=1



# create a list of even numbers between 10 to 30 and print the list
# ls = []
# for i in range(10,31):
#     if i%2 == 0:
#         ls.append(i)
# print(ls)

# # Check a given word whether it is palindrome or not!! True if yes other false
# word = "Sriharsha"
# 
#"ahsrahirs"
# word = word.lower()# with out slicing

# take input from user a list of  integer values which are Temperatures recorded in last 7 days and find the average temperature
# ls = []
# for i in range(1,8):
#     user_input = int(input(f"Enter your input{i}:"))
#     ls.append(user_input)
# print("List of integers from user: ",ls)
# avg = sum(ls)/7
# print(avg)




#Problem: Create a simple countdown from 10 to 1 and then print "Liftoff!".

# countdown = 10

# while countdown > 0:
#     print(countdown)
#     countdown -= 1

# print("LiftOff")

#Continuously ask the user to enter their age until they provide a valid number (age must be between 1 and 120).

# age = int(input("Enter your correct age?: "))

# while age<1 or age>120:

#     age = int(input("Enter your correct age?: "))




#: Create a simple game where the computer randomly chooses a number between 1 and 100, 
# and the user has to guess it. The program should provide feedback ("too high" or "too low") 
# until the user guesses the number correctly.

# hidden = 20

# num = 95

# while num != hidden:
#     num = int(input("Enter the Secret number?(between 1 to 100): "))

#     if num > hidden:
#         print("too high")
#     elif num < hidden:
#         print("too low")
#     else:
#         print("Correct")


#Problem: Implement a system that allows a user up to three attempts to enter a correct password.
#  If the user fails to enter the correct password after three attempts, the system should lock them out and
#  display an appropriate message.

# password = "something"

# attempts = 3
# while attempts>0:
#     user_pass = input("Enter Your password?: ")
#     if password == user_pass:
#         print("password Correct")
#         break
    
#     else:
#         attempts -= 1

#     if attempts == 0:
#         print("Incorrect password given multiple times! Access Denied")






