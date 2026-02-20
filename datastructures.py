
a = [1,2,3]

print(a)

len = len(a)

print("Lenght of a "+str(len))

a[len:] = [4] # Equal to a.append(4)

print(a)
# list append method
a.append(5)

print(a)
# list extend method
a.extend([6,7,8])

print(a)
# list insert method
a.insert(0,0)

print(a)
# list remove method
a.remove(0)

print(a)

lastdigit = a.pop()

print(a)
print(lastdigit)


print(a.reverse())


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting at position 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()


squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = []
squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = []
squares = [x**2 for x in range(10)]
print(squares)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])