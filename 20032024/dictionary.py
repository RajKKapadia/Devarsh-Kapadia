'''Dictionary
key -> value pairs
name -> Rajesh
age -> 23
'''

# Defining dictionary
d = {
    'name': 'rajesh',
    'age': 23,
    'hobby': ['cricket', 'chess'],
    'books': {
        1: 'Book one',
        2: 'Book two'
    },
    'flag': True 
}
print(d)
# print(d)
# print(type(d))
# Access aby key
# print(d['books'])

# print(d.items())

# # print(d.keys())
# # Update value
# d['name2'] = 'Ramesh'
# print(d)

# # Add new key value pair
# d['New key'] = 'New value'
# print(d)
# '''NOTE:
# if the key is not prsent in the dictionary, it will add a new key pair
# '''
# d.update({'name': 'Mahesh'})
# print(d)

# d.update({'name1': 'Mahesh'})
# print(d)

# Remove a key value pair by key
d.pop('flag')
print(d)

d.popitem()
print(d)

# Get the value of a key
print(d.get('name1', 25))
print(d['name'])

d.clear()
print(d)