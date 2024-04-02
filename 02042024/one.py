# '''Print cube of number less than 10
# 1 8 27 64 125 ...
# '''
# for i in range(1, 11):
#     print(i**3)

# cubes = [i**3 for i in range(1, 11)]
# print(cubes)

a = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 1, 2, 1]
n = 1
count = 0
# for i in a:
#     if i == n:
#         count += 1
# print(count)
x = [2 for i in a if i == n]
print(x)
for y in x:
    count += y