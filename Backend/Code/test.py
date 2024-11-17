# # # Armstrong
# # # num = input('Enter the number') # String

# # num = '153'
# # power = len(num)
# # # digits_powers = [int(i)**power for i in num]
# # digits_powers_sum= 0


# # for i in num:
# #     val = int(i)**power
# #     print(val)
# #     digits_powers_sum += val



# # # final_sum = sum(digits_powers)

# # if digits_powers_sum == int(num):
# #     print("Armstrong")
# # else:
# #     print("Its not Armstrong")


# # # def arm_strong(num):
# # #     digits = num.split()
# print("Debug Started")
# try: 
#     num = int(input("Enter a numerator"))
#     den = int(input("Enter the denominator"))
#     result= num/den
# except ZeroDivisionError:
#     print("Error : Cannot divide with Zero")
# except ValueError:
#     print("Error: Invalid values entered please enter numbers only")
# else:
#     print(f"Result: {result}")
# finally:
#     print("Finally block ")

# # print("Debug Stopped")

# def check_age(age):
#     if age <0:
#         raise ValueError("Age cannot be less than Zero")
#     else:
#         print(age)

# try:
#     check_age(-10)
# except ValueError as e:
#     print(e)

# Divide Two Numbers with Exception Handling​

# Write a function that takes two numbers as input and returns their division. 
# Include exception handling for division by zero and invalid input types.

# Multiple Exceptions in List Operations​

# Write a function that takes a list and an index as input and returns the element at that index. 
# Handle exceptions for index out of range and invalid index type

def list_elements(lst,inx):
    try:
        return lst[inx]
    except IndexError:
        return "Error: index Out of range"
    except TypeError:
        return "Error: invalid index type"


print(list_elements([1,2,3],1))
print(list_elements([1,2,3],9))
print(list_elements([1,2,3],'a'))