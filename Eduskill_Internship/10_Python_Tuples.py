empty_tuple = ()

coordinates = (10.0, 20.0)
colors = ('red', 'green', 'blue')
mixed_tuple = (1, 'hello', True)

single_element_tuple = (42,)
not_a_tuple = (42)  # integer

colors = ('red', 'green', 'blue', 'yellow', 'purple')   # index and slicing

print(colors[0])    # red
print(colors[-1])   # purple

print(colors[1:4])  # ('green', 'blue', 'yellow')
print(colors[::2])  # ('red', 'blue', 'purple')

colors = ('red', 'green', 'blue')
# colors[0] = 'orange'  Error
