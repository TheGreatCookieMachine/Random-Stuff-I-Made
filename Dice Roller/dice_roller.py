import random


while True:
    place = 0
    dice = 0
    sides = 0
    result = []
    print('Please input your dice roll in the following style:')
    print('<Amount of dice>d<Sides on the Dice>')
    print('For example 3d5 will roll 3 5 sided dice and 9d7 will roll 9 7 sided dice.')
    path = input()
    while True:
        if 'd' in path.lower()[place+1]:
            dice = int(str(dice) + path[place])
            break
        else:
            dice = int(str(dice) + path[place])
            place = place + 1
    place = place + 2
    while place < len(path):
        sides = int(str(sides) + path[place])
        place = place + 1
    while len(result) < dice:
        result.append(random.randint(1, sides))
    print(result)
