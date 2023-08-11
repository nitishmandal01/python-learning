from math import *

# # S1 D3 Assignment - Set 1

# ## Set 1

# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"

print("Hello World!")

# ****************************************************************

# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, , set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."

name = "Nitish"
name_type = type(name)

age=22

floatValue = 1.5

bolleanValue = True

listEx = [10,9,8,7]

tupleExample = (2,5,8,6)

dictionary = {"java": 10, "JS": 9, "HTML": 9, "CSS": 9}

# print("TYpe of name is: "+ str(name_type))
print("TYpe of name is: ", type(name))
print("TYpe of age is: ", type(age))
print("TYpe of name is: ", type(floatValue))
print("TYpe of name is: ", type(bolleanValue))
print("TYpe of name is: ", type(listEx))
print("TYpe of name is: ", type(tupleExample))
print("TYpe of name is: ", type(dictionary))

# **********************************************************************************

# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."
numbers = [1,2,3,4,5,6,7,8,9,11,10,11]
numbers.append(20)
print(numbers)
print("*****After removal********")
numbers.remove(11) #It removed the number itself, no matter any position....if 2 numbers presnet, remove first occurance
numbers.pop(0)
print(numbers)




# **********************************************************************************
# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"
numbersList =  [10, 20, 30, 40]

sum = 0
for x in numbersList:
    sum+=x

count = len(numbersList)
print("Sum is: ",sum, "Average is: ", sum/count)


# **********************************************************************************
# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

# inputString = input("Write the String here:")
def reverseString(str):
    x=len(str)-1
    rev=""
    while(x>=0):
        rev+=inputString[x]
        x-=1
    return rev

# reversedString = reverseString(inputString)
# print(reversedString)


# **********************************************************************************
# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"
# inputStr = input("Write your Word: ")

def numberOfVowel(str):
    vowel=0
    for char in str:
        if char.lower() in "aeiou":
            vowel+=1
        elif char.upper() in "AEIOU":
            vowel+=1

    return vowel


# stringHaveVowels = numberOfVowel(inputStr)
# print("Number of Vowels in your given String is", stringHaveVowels)
# **********************************************************************************
# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

# input2 = input("Write down the number: ")
# inputNumber = int(input2)

def checkPrime(x):
    i=2
    while(i<=sqrt(x)):
        if(x % i == 0):
            return False
        i+=1
    return True


# checkPrimeOrNot = checkPrime(inputNumber)
# print(checkPrimeOrNot)

# **********************************************************************************
# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

# input3 = input("Write down the number: ")
# factInput = int(input3)

def factorial(x):
    i=1
    fact=1
    while(i<=x):
        fact*=i
        i+=1
    return fact

# fact = factorial(factInput)
# print("Factorial of ",factInput, " is ",fact)



# **********************************************************************************
# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"
input4 = input("Write down the number: ")
fibInput = int(input4)

def fib(n):
    fibList = [0, 1]
    for i in range(2, n):
        next_num = fibList[-1] + fibList[-2]
        fibList.append(next_num)
    return fibList


fibList = fib(fibInput)
print(fibList)

# **********************************************************************************
# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"

sqList = []

for x in range(1,11):
    sq = x**2
    sqList.append(sq)

print(sqList)
