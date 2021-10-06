def greeting(name):
    print('Hello', name)

greeting('Erin')
greeting('Paolo')
greeting('Tanya')

def about_me(fave_food, fave_animal, fave_place):
    print('I love to eat', fave_food, 'while petting my', fave_animal, 'at', fave_place)

about_me('sushi', 'cat', 'the beach')

about_me('the beach', 'sushi', 'cat')

about_me(fave_place='the beach', fave_food="sushi", fave_animal='cat')

def accept_phone(number, phone_type):
    print('The phone number', number, 'is a', phone_type, 'phone')

accept_phone('555-1234', 'home')
accept_phone('555-5678', 'cell')
accept_phone('555-8765', 'work')


def accept_phone_number(number, phone_type='cell'):
    print('The phone numba', number, 'is a', phone_type, 'phone')

accept_phone_number('555-1234', 'home')
accept_phone_number('555-5678', 'cell')
accept_phone_number('555-8765', 'work')

accept_phone_number('555-1122')

def greeting():
    print('Hello', name)

name = 'Marco'
greeting()

def greeting_a():
    name_a = 'Maria'
    print('Hello', name_a)

name_a = 'Marco'
greeting_a()

def greeting_b():
    global name_b
    print('Hello', name_b)
    name_b = 'Maria'
    print('Hello', name_b)

name_b = 'Marco'
greeting_b()
