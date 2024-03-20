'''TODO
[] try by yourself the following methods of list
pop()
remove()
reverse()
sort()
'''

# Tuple
# Initialize a tuple
# l = [1, 2, 3, 4, 5, 'String', 23.45, False, [1, 2, 3]]
# t = tuple(l)
# print(t)
# print(type(t))

# t = (1, 2, 3, 4, 5, 'String', 23.45, False, [1, 2, 3])
# print(t)
# print(type(t))

# # How to access value from index
# print(t[6])
# # This can not be possible
# t[0] = 25

# t = (1, 2, 3, 4, 5, 'String', 23.45, False, [1, 2, 3])
# print(t)
# print(type(t))

# # You can not perform the following actions on tuple, so we convert it to list and perform the actions
# l = list(t)
# l.append('Last')
# l.remove('String')

# t = tuple(l)
# print(t)
# print(type(t))

# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

t = (10, 20, 10, 40, 50, 10)

# a, b, _ = t
# print(a)
# print(b)
# print(c)

print(t.count(10))

# This takes two more arguments
# start index from where you want to start the search
# end where you want to stop the search
# it returns the original index of the value
print(t.index(10, 3))