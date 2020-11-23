print("************************************************")
print("************************************************")
print("************************************************")
# Interview Question 1
def string_times(str, num):
  ''' Write a Function which takes two arguments string and non-negative integer and return the given string times what the integer value is '''
  if num <= 0:
    print("Invalid Number")
  return str * num
print(string_times("Muhammad\n", 3))

print("************************************************")
print("************************************************")
print("************************************************")

# Interview Question 2
def name_function(name):
  ''' Create a Function which takes one argument as a name and Sends Greetings '''
  return "Hello " + name + ".\nThank you for using codingbat.com"
print(name_function("Muhammad SHakir"))

print("************************************************")
print("************************************************")
print("************************************************")
# Interview Question 3
def first_and_last_number(number):
  ''' Check the List the first and List number is 6, If so --> Return True '''
  if number[0] == 6 and number[-1] == 6:
    return True
  else:
    return False

print(first_and_last_number([6,4,5,6]))
print(first_and_last_number([6,4,5,5]))
print(first_and_last_number([4,5]))

print("************************************************")
print("************************************************")
print("************************************************")
# Interview Question 4
def string_times2(str):
  ''' Function will return the given string character * 2 '''
  to_return = ""
  for charac in str:
    to_return += charac * 2
  return to_return
print(string_times2("A-B-C-D-E"))

print("************************************************")
print("************************************************")
print("************************************************")
# Interview Question 5
def count_even(nums):
  ''' Write a function which accept list as an argument and count number of even numbers from the list '''
  count = 0
  for x in nums:
    if x % 2 == 0:
      count += 1
  return count
print("There are", count_even([2,4,6,8,10,1,3,5,7,9]), "Even Number(s) in the list")

print("************************************************")
print("************************************************")
print("************************************************")
# Interview Question 5
def count_odd(nums):
  ''' Write a function which accept list as an argument and count number of odd numbers from the list '''
  count = 0
  for x in nums:
    if x % 3 == 0:
      count += 1
  return count
print("Count Odd Number: ",count_odd([6,8,10,3,5,7,9,11,12]))

print("************************************************")
print("************************************************")
print("************************************************")

def true_false(a, b, negative):
  ''' By Using the Range, Find out the return number will return True or False '''
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

print(true_false(-11, -1, True))

print("************************************************")
print("************************************************")
print("************************************************")
