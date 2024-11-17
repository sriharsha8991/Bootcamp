#Strings
#1. Write a Python program to find words which are greater than given length k?

# words = ["Sri","Python","Sathvik","Teja"]
# k = 4
# c=0
# # output as 2
# for i in words:
#     if len(i)>k:
#         print(i)
#         c+=1
# print(c)



# 2. Write a Python program for removing i-th character from a string?
# word = "PIShapers"
# ith = 5
# dummy = ""
# for i in range(len(word)):
#     if i==ith:
#         continue
#     dummy += word[i]
# print(dummy)


# 3. Write a Python program to split and join a string?


# sent = "Python is a popular Programming Language, Especially for Data Science"
# v = sent.split(" ")


# print("".join(v))


# 4. Write a Python to check if a given string is binary string or not?

# wrd = "010101"

# for i in wrd:
#     if i != "0" or i!="1":
#         print("Not a binary String")
#         break


# 5. Write a Python program to find uncommon words from two Strings?

# st1 = "Sri is python Dev"
# st2 = "Sri is c++ programmer"


# for i in st1.split(" "):
#     for j in st2.split(" "):
#         if i not in j:




# 6. Write a Python Program to find all duplicate characters in string?

# St = "Sriharsha"
# lwer = St.lower()
# ans = ""

# for i in lwer:
#     if lwer.count(i)>1 and (i not in ans):
#         ans += i
# print(ans)



# 7. Write a Python Program to check if a string contains any special character?

# st = "srizkbjf658"
# if st.isalnum() == True:
#     print("All the Characters are alpha numeric")
# else:
#     print("String has special Characters")










# Question 1:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated
# sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# c=50
# h=30
# # d = 1
# d = input("Enter the Values: ")
# numbers = d.split(",")
# ans = []
# for d in numbers:
#     form = ((2*c*int(d))/h)**0.5
#     ans.append(str(int(form)))
# print(",".join(ans))













# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# map
# inputs = input("Enter the values").split(",")
# f = inputs[0]
# s = inputs[1]
# ans = []
# for i in range(f):
#     row = []
#     for j in range(s):
#         row.append(i*j)
#     ans.append(row)
# print(ans)







# Question 3:
# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# st = input("Enter the Comma Seperated words: ").split(",")
# st.sort()
# print(",".join(st))


# Question 4:
# Write a program that accepts a sequence of whitespace separated words as input and prints
# the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# st = input("Enter the String: ").split(" ")

# st = list(set(st))
# st.sort()
# print(" ".join(st))


# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# st = input("Enter the phrase: ")
# Letters = 0
# Digits = 0
# for i in st:
#     if i.isalpha() == True:
#         Letters += 1
#     elif i.isnumeric() == True:
#         Digits += 1

# print("LETTERS ",Letters)
# print("DIGITS ",Digits)




# Question 6:
# A website requires the users to input username and password to register. Write a program to
# check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
#
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,
# a F1#,
# 2w3E*,
# 2We3345
# Then, the output of the program should be:
# True or False



#List
# 1. Write a Python program to find sum of elements in list? do not use built in Functions.
#input = [1,2,3,4,5,6]
#output :21
# ls = [1,2,3,4,5,6]
# add = 0
# for num in ls:
#     add+= num
# print(add)



# 2. Write a Python program to Multiply all numbers in the list?


# ls = [1,2,3,4,5,6]
# add = 1
# for num in ls:
#     add*= num
# print(add)

# 3. Write a Python program to find smallest number in a list?
# ls = [1,2,3,4,5,6,0]
# print(min(ls))
# ls.sort()
# print(ls[0])



# 4. Write a Python program to find largest number in a list?
# ls = [4,2,5,3,9,8,1]
# maxi = -1
# for i in ls:
#     if i>maxi:
#         maxi = i
# print(maxi)

# 5. Write a Python program to find second largest number in a list?







# 6. Write a Python program to find N largest elements from a list?
# 7. Write a Python program to print even numbers in a list?
# 8. Write a Python program to print odd numbers in a List?
# 9. Write a Python program to Remove empty List from List?
# 10 . Write a Python program to Count occurrences of an element in a list?