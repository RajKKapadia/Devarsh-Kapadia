# List
'''List can be created using []
[0, 1, 2, 3, ...]
'''
a = ['First', 1, False, 'Hello', 25.25, [1, 2, 3], 'Another sting', 'Eighth']
print(a)
print(type(a))
print(len(a))
# get the value by index/location
print(a[7])
# replace value at a location
a[0] = 'Ramesh'
print(a)
# Add new values in the end
a.append('New item')
print(a)
a.append('Last')
print(a)
# Insert new value at a location
a.insert(0, 'First added')
print(a)
# Get location/index of a value
print(a.index('False'))