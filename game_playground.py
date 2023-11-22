#CYPHER
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def find_index(letter):
    if letter != ' ':
        position = letters.index(letter.lower())
        return position + 1

def splitter():
    user_input = input('what is the code? ') # gets input from user
    seperate_letters = list(user_input) # splits letters into a list
    seperate_index = list(map(find_index, seperate_letters)) # iterates through letters and returns a integer find_index
    res = list(filter(lambda n: n != None and n > 0 and n < 27, seperate_index)) # filters out none values and numbers between 0 and 27 (index) positions
    isMatch = compare_arrays(res)
    return isMatch

def compare_arrays(array):
    result = [16, 25, 20, 8, 15, 14] # python
    sorted(result) # sort arrays
    sorted(array)
    if result == array: # compare arrays 
        return 'match'
    else:
        return 'no match'

# MAZE
# oxxxxxxx
# oxooooxx
# oxoxooxo
# oxoxoxxo
# oooxoooo
# each line 8
# |       |       |       |       |
# oxxxxxxxoxooooxxoxoxooxooxoxoxxooooxoooo
maze = 'oxxxxxxxoxooooxxoxoxooxooxoxoxxooooxoooo'
place = int(input('index '))
print(maze[place] + '\n' + maze[place % 8] + '\n' + maze[place % -8])

# above position is - 8
# below position is + 8
# right position is + 1
# left position is - 1