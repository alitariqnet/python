print("Hello, World!")
# 
print(17/3)
print(17//3)
print(17%3)
print(++17)
print(--17)

print(2 + 2)

print(50 - 5*6)

print((50 - 5*6) / 4)

print(8 / 5)  # division always returns a floating-point number

print(5 ** 2)  # 5 squared

print(2 ** 7)  # 2 to the power of 7

width = 20
height = 5 * 9
print(width * height)
# If a variable is not “defined” (assigned a value), trying to use it will give you an error:
# n
# print(n)

tax = 12.5 / 100
price = 100.50
print(price * tax)

# print(price + _)

# print(round(_, 2))

print('spam eggs')  # single quotes

print("Paris rabbit got your back :)! Yay!")  # double quotes

print('1975')  # digits and numerals enclosed in quotes are also strings

print('doesn\'t')  # use \' to escape the single quote...

print("doesn't")  # ...or use double quotes instead

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string

print(s)  # with print(), special characters are interpreted, so \n produces new line

print('C:\some\name')  # here \n means newline!


print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')
print('Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print(text[0])
print(text[-2]) # Second char from right to left
print(text[-1]) # First char from right to left


word = 'Python'
word[0]  # character in position 0

word[5]  # character in position 5

word[-1]  # last character

word[-2]  # second-last character

word[-6]

word[-1]  # last character

word[-2]  # second-last character

word[-6]

word[0:2]  # characters from position 0 (included) to 2 (excluded)

word[2:5]  # characters from position 2 (included) to 5 (excluded)

word[:2]   # character from the beginning to position 2 (excluded)

word[4:]   # characters from position 4 (included) to the end

word[-2:]  # characters from the second-last (included) to the end

word[:2] + word[2:]

word[:4] + word[4:]

print("""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
""")

'J' + word[1:]

word[:2] + 'py'

s = 'supercalifragilisticexpialidocious'
print(len(s))

# LISTS

squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])  # indexing returns the item

print(squares[-1])  

print(squares[-3:])  # slicing returns a new list

print(squares + [36, 49, 64, 81, 100])

squares.append(99)

print(squares)
print(squares[2])
print(squares[-1])

cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!

cubes[3] = 64  # replace the wrong value
print(cubes)

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes
print(cubes)

# Object referencing 
rgb = ["Red", "Green", "Blue"]
rgba = rgb
same = id(rgb) == id(rgba)  # they reference the same object
print(same)
rgba.append("Yellow")
rgba.append("Alph")
print(rgb)
# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:
# Shallow copy
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)

print(rgba)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])

print(x[0][1])

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
    print(a, end=', ')
    a, b = b, a+b


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


print(active_users)