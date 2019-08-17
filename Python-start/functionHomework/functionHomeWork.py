# 1

name = 'Василий'
age = 21
city = 'Москва'

def people_information(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)

print(people_information(name, age, city))

# 2

number_one = 3
number_two = 2
namber_three = 4

def max_number(*args):
    return max(*args)

print(max_number(number_one, number_two, namber_three))

# 3, 4
player_name = input('Введите имя игрока: ')
enemy_name = input('Введите имя врага: ')

player = {
   'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy = {
   'name': enemy_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

def attack(player, enemy):
    player['damage'] = clean_damage(player['damage'], enemy['armor'])
    enemy['health'] = enemy['health'] - player['damage']
    print(f'Остаток здоровья врага: ', enemy['health'])

def clean_damage(damage, armor):
    return damage / armor


attack(player, enemy)
