# #Function with out parameters
# def fun():
#     name = "Sriharsha"
#     print(f"{name} is a python Developer")

# fun()
# # With parameters
# def fun(name):
    
#     print(f"{name} is a python Developer")

# fun("Sathvik")

# # Functions with mutliple parameters
# def fun(age,name="Prudhvi"):
    
#     print(f"{name} is a python Developer whose age is {age}")

# # fun("Sri",24)# Arguments are "Sri",24(Positional Arguments)

# fun(age=36,name="Sree")
# #Keyword Arguments

# def evens(*nums):
#     for i in nums:
#         if i%2==0:
#             print(i)
# evens(1,2,3,4,5,6,7)

# def kwargs(**kk):
#     for i in kk.keys():
#         print(i)
    
# kwargs(age=36,name="Sree")



# def add(a,b):
#     """this function is responsible for returning three outputs
#     first one as added value of two parameters second one is substraction value 
#     and third one is product of two parameters"""
#     return a+b,a-b,a*b
# help(add)
# f1,f2,f3 = add(5,1)

# print(f1,f2,f3)

# def fun(*args):
#     count = 0
#     for numbers in args:
#         count = count + numbers
        
#     return count


# f1 = fun(8,2,3,0,7)
# print(f1)











# Write a function sum_of_squares(n) that calculates the sum of the squares of 
# the first n natural numbers. Use a helper nested function 
# to calculate the square of a number.
# Main target: Finding Sum of Squares
#---> square of number
# find the sum of the squared numbers

# def sum_of_squares(n):

#     def square(num):
#         return num**2
    
#     ans = 0
#     for i in range(1,n+1):
#          ans += square(i)

#     return ans

# res = sum_of_squares(3) # 1+4+9 = 14
# print(res)


#Q2: Write a function longest_word(sentence) that takes a sentence 
# and returns the longest word in it.
#  Use a nested functions to split the sentence into words.

#split inner function
# list of words
# for loop on words

# def longest_word(sent):

#     def split_sent(x):
#         return x.split(" ")
    
#     ls_words = split_sent(sent)
#     dumm = ""
#     for word in ls_words:
#         if len(word)> len(dumm):
#             dumm = word
#     return dumm
    

# sentence = "Use a nested functions to split the sentence into words"
# ans = longest_word(sentence)
# print(ans)




# Write a function count_vowels(words) that takes a list of words and 
# returns a list of the number of vowels in each word.
# Use a nested function to count vowels in a single word.
# def count_vowels(words):

#     def count_vowels_in_single_word(x):
#         vowels="aeiouAEIOU"
#         count=0
#         for i in x:
#             if i in vowels:
#              count=count+1
#         return count
    
#     ans = []
#     for i in words:
#        vowel_count = count_vowels_in_single_word(i)
#        ans.append(vowel_count)

#     return ans

# ip = ["Sathvik","Sri","Prudhvi"]
# ans = count_vowels(ip)
# print(ans)
       






# Write a function filter_even_numbers(numbers) that takes a list of numbers 
# and returns a list of even numbers.
#  Use a nested function to check if a number is even.

# def filter_even(numbers):

#     # def even(x):
#     #     return x%2 == 0
#     def even(x):

#         if x%2==0:
#             return True
#         return False
    
#     ans = []
#     for i in numbers:
#         if even(i):
#             ans.append(i)

#     return ans

# numbers = [1,2,3,4,5,6,7,8,9]
# print(filter_even(numbers))



# def even(c):
#     return c%2 == 0

# def get_evens(numbers):
#     ans = []
#     for i in numbers:
#         if even(i):
#             ans.append(i)
#     return ans

# numbers = [1,2,3,4,5]

# print(get_evens(numbers))









#Write a function factorials(numbers) that takes a list of numbers 
# and returns a list of their factorials. 
# Use a multiple function to calculate the factorial of a single number.
# op = [1,2,6,24,120]


#Create a function for Finding the Factorial of a number .
# def factorial(n):
#     count=1
#     for number in range(1,n+1):
#         count *= number
#     return count


# def op_factorials(numbers):
#     ans = []
#     for num in numbers:
#         fact = factorial(num)
#         ans.append(fact)
#     return ans


# numbers = [1,2,3,4,5]
# print(op_factorials(numbers))


# map,zip,lambda,filter......(inbuilt)

#lambda function  #small anonymous function
# def res(x):
#     return x+10

# res = lambda x : x+10
# print(res(10))
# def ans(x,y):
#     return x*y

# ans = lambda x,y: x*y
# print(ans(10,5))

# for_three = lambda x,y,z : x+y+z
# print(for_three(10,2,9))


# def fun1(n):
#     return lambda a : a*n

# res = fun1(2) # lambda a : a*2
# print(res(11)) # Output 22













#Write a function convert_to_fahrenheit(celsius) that takes a 
# list of temperatures in Celsius and 
# returns a list of temperatures converted to Fahrenheit 
# using map() and a lambda function.​

# def convert_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# temp = [0,20,37,100]
# print(list(map(convert_to_fahrenheit,temp)))



# Write a function filter_odd(numbers) that takes a list of numbers 
# and returns a list of only the odd numbers using filter() 
# and a lambda function.​

​# Write a function calculate_squares(numbers) that takes a 
# list of numbers and returns a list of their 
# squares using map() and a lambda function.​

#Write a function filter_and_square_even(numbers) that takes a list of numbers and 
# returns a list of squares of the even numbers using filter(), map(), 
# and lambda functions.​