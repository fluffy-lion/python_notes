# Expressions

# numeric expressions

# + add
print(2 + 3)
# - sub
print(5 - 3)
# * multiply
print(2 * 3)
# / division
print(6 / 3)
# ** power
print(4 ** 3)
# % remainder
print(6 % 4)

# order of evaluation
# adding strings together, python must know which one to do first, operator precedence

# parenthesis       |
# power             |
# multiplication    |
# addition          |
# left to right     \/

# types
# python knows the difference between an integer and a string
# + will add and integer
# + will concatenate a string

# may get traceback, programe is confused
#

eee = 'hello ' + 'there'
# tells us type
print(type(eee))
print(type(1))

# two types of numbers
# integers are whole
# floating point have decimal parts

# type conversions with built-in functions
# when you put an integer and floating point in an expression the integer is implicitly converted to a float
num1 = float(99)
num2 = 100
print(type(num2))
res = num1 + num2
print(type(res))

# integer division
# always produces a floating point result 
# this was differnt in Python 2.x

# String Conversions
# can use int() and float() to convert between strings an integers
# will get an error is the string does not contain numeric characters

# input
# can instruct Python to pause and read date from user using input()
# nam = input('who are you? ')
# print('welcome', nam)

inp = input('Europe floor? ')
usf = int(inp) + 1
print('US floor', usf)