# more complex condition statements

# multi-way branch3 like the if and else but 
# now can add multiple conditions
# check them in order
# only one of these three will be executed in this block
x = 3
if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print('large')
print('all done')

# can have a no else
# means that you arent guaranteed that one if going to run 
x = 5
if x < 2:
    print('small')
elif x < 10:
    print('medium')

# can also have many elifs 
# important to be sure with the order you have put them in

# the try and except structure 
# you surround a dangerous section of code with try and except
# if the code in the try works - the except is skipped
# if the code in the try fails - it jumps to the except section

# astr = 'hello bob'
# istr = int(astr)

# if the code blows up
# may want to try and except a piece of code

astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print('first', istr) # drops into the except, and program continues

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('first', istr) # if it succeeds it just skips the except and program continues

# dont overuse, more than one line it may never get used
# which ever line blows up, that is the last line that gets executed in that block

rawstr = input('enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('nice work')
else:
    print('not a number')