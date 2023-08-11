# # S1 D3 Assignment - Set 2

# *******************************************************************************
# ### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.

# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ```
print("Hello World")
i=1
while i<=5:
    ans=""
    j=1
    while j<=i:
        ans+=str(j)+" "
        j+=1
    i+=1

    print(ans)


# *******************************************************************************
# ### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

# **Given**:

# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```

# **Expected output:**

# ```
# 75
# 150
# 145
# ```

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)

# *******************************************************************************
# ### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```

# **Expected Output**:

# ```
# AuKellylt
# ```

s1 = "Ault"
s2 = "Kelly"
mid = int(len(s1)/2)
s3 = s1[:mid] + s2 + s1[mid:]
print(s3)


# *******************************************************************************

# ### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:

# ```
# yaivePNT
# ```
str1 = "PyNaTive"
low=""
big=""
for x in str1:
    if x == x.lower():
        low+=x
    else:
        big+=x

print(low+big)


# *******************************************************************************
# ### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:

# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```

# **Expected output:**

# ```
# ['My', 'name', 'is', 'Kelly']
# ```

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
ans=[]
minIndex = min(len(list1), len(list2))
i=0
while i<minIndex:
    word = list1[i]+list2[i]
    ans.append(word)
    i+=1

if len(list1) > minIndex :
   ans.extend(list1[minIndex:])
elif len(list2) > minIndex:
    ans.extend(list2[minIndex:])


print(ans)

# *******************************************************************************

# ### Problem **6: Concatenate two lists in the following order**

# ```
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ```

# **Expected output:**

# ```
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# ```
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
ans=[]
for i in list1:
    for j in list2:
        msg=i+j
        ans.append(msg)

print(ans)

# *******************************************************************************
# ### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# **Given**

# ```
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# ```

# **Expected output:**

# ```
# 10 400
# 20 300
# 30 200
# 40 100
# ```

list1s = [10, 20, 30, 40]
list2s = [100, 200, 300, 400]

for x, y in zip(list1s, reversed(list2s)):
    print(x,y)



# *******************************************************************************
# ### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

# **Given**:

# ```
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# ```

# **Expected output:**

# ```
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
# ```


# *******************************************************************************
# ### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# **Given dictionary**:

# ```
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# ```

# **Expected output:**

# ```
# {'name': 'Kelly', 'salary': 8000}
# ```


# *******************************************************************************
# ### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:

# ```
# tuple1 = (11, [22, 33], 44, 55)
# ```

# **Expected output:**

# ```
# tuple1: (11, [222, 33], 44, 55)
# ```