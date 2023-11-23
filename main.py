# conditional execution

# 
# beginning of having python make a decision for us
# if statement, reserved word
# produces a yes or not result which we use to control program flow

x = 5
if x < 10:
    print('Smaller') # either runs or doesnt
if x > 20:
    print('Bigger')
print('finish')

# comparison Operators, they look but don't chnge the variables
# < less than
# <= less than or equal to
# == equal
# > more than
# >= more than or equal to
# != not equal

# as long as you stay indented it is still in the if block
# if it isnt it will skip
if x == 5:
    print('is 5')
    print('is still 5')
    print('third 5')

# indentation
# syntactically correct
# you maintain the indent to indicate the scope of the block

# blank lines are ignored

# increase / maintain after if or for
# decrease to indicate end of block

# nested decisions
x = 42
if x > 1:
    print('more than one')
    if x < 100:
        print('less than 100')
print('all done')

# two way decisions
# sometime we want to do one thing if a logical expression is true3 and something else if the expression is false
# its like a fork in the road, choose one or the other
# ends up being part of the whole block
x = 3
if x > 2:
    print('bigger')
else:
    print('smaller')
print('all done')
