'''Two main loops
while
for
'''
'''Loop means do something repeatedly until some condition matches or do something for a fixed numbers of time
while -> until some condition is fulfilled do something
for -> repeat some action for a fixed number of times
'''

'''while
while condition
    code
    MOST IMPORTANT THING
    condition either True/False
'''

# a = 5

# while a > 0:
#     print(f'Value of A - {a}')
#     a -= 1
#     print('A is greater than 0.')

'''for
for counter:
    code

    repeat itself for the counter
There are multiple ways to provide the counter
'''
# range(start, stop, interval)
# stop is not included
# print(range(10))

# for i in range(10):
#     print(i)

# l = [132, 32322, 2323, 32314, 2315, 23136, 732213, 3138, 3139]
# for item in l:
#     print(item)
# for i in range(len(l)):
#     print(l[i])
    
# t = (11, 22, 33, 44, 55)
# for item in t:
#     print(item)
# for i in range(len(t)):
#     print(t[i])

d = {
    'name': 'Rajesh',
    'age': 25,
    "isWorking": True,
    "Salary": 1234.55
}

# for i in range(len(d)):
#     print(d[i])

'''unpack tuple
a, b, c = (1, 2, 3)
'''

for k, v in d.items():
    print(k, v)