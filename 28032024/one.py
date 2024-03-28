# l1 = [2, 3, 4, 5]
# l2 = [2, 5, 6, 7]

# for i in range(len(l1)):
#     print(f'Value of i -> {i}')
#     print(f'Value of l1[i] -> {l1[i]}')
#     print(f'Value of l2[i] -> {l2[i]}')
#     if l1[i] in l2:
#         print(l1[i])

def get_factors(n):
    factors = []
    x = 2
    for i in range(2, n + 1):
        if n == 1:
            break
        elif n % x == 0:
            factors.append(x)
            n //= x
        else:
            x += 1
    return factors


n1 = int(input('Enter a number - '))
n2 = int(input('Enter a number - '))

factors1 = get_factors(n1)
print(factors1)

factors2 = get_factors(n2)
print(factors2)


