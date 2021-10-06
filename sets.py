unique_colors = ['red', 'yellow', 'red', 'green', 'red', 'yellow']
subscribed_emails = ['mary@gmail.com', 'opal@gmail.com', 'mary@gmail.com', 'sayed@gmail.com']

# my_set = set(a_list_to_convert)
unique_colors_set = set(unique_colors)
print(unique_colors_set)

# my_set_2 = (['enter', 'list', 'here'])
unique_colors_set_2 = set(['red', 'yellow', 'red', 'green', 'red', 'yellow'])

clothing_list = ['red', 'yellow', 'red', 'green', 'red', 'yellow']

clothing_set = set(clothing_list)
print(clothing_set)

# In a list:
clothing_list.append('red')

# In a set 
clothing_set.add('red')

for i in clothing_list:
    print('clothing_list', i)

for i in clothing_set:
    print('clothing_set', i)

# In a list:
clothing_list.pop() # Removes and returns the last item in the list.
clothing_list.pop(0) # Removes and returns a specific (here, the first) item in the list.

# In a set
clothing_set.pop() # No! This is a unreliable! The order is arbitrary.
clothing_set.pop(0) # No! Python throws an error! You can't index sets.
clothing_set.remove('red') # Do this! Call the element directly!



