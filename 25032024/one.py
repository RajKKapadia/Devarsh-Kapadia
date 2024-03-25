'''Print the following pattern
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
'''
'''
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
'''
n = int(input('Enter a number - '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')

# n = str(input('Enter your name - '))

# for i in range(len(n)):
#     for j in range(i):
#         print(n[j], end=' ')
#     print('')
