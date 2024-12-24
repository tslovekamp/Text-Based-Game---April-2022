'''
Name: John Kimmell
Assignment: 145 Project
Date: 4/20/2022
'''

import ActionsFile
import random

player1 = ActionsFile.Actions()
player2 = ActionsFile.Actions()

player1_name = str(input("Enter player 1's name here: "))
player2_name = str(input("Enter player 2's name here: "))

player1.setPlayerName(player1_name)
player2.setPlayerName(player2_name)
player1.setHealth(100)
player2.setHealth(100)

class playerCheck():

    _player1 = ''
    _player2 = ''

    def __init__(self):
        _player1 = ''
        _player2 = ''

    def get_player1(self):
        return self._player1

    def get_player2(self):
        return self._player2

    def set_player1(self, player_1):
        self._player1 = player_1

    def set_player2(self, player_2):
        self._player2 = player_2

    def __str__(self):
        return 'TO-DO'

    def check_health(self, player, health):
        if health <= 0:
            if player._guardianAngel >= 1:
                player.useGuardianAngel()
            else:
                print("You died!")
                return 0
        else:
            return health
    def check_potion(self, potion):
        if potion <= 0:
            return 0
        else:
            return potion

    def rand_funct(self, rand_value, guess):
        if guess == rand_value:
            return 0
        else:
            return 1
    def choose_method_1(self, rand):
        if rand == 1:
            player1.increasePotion()
        elif rand == 2:
            player1.stubbedToe()
        elif rand == 3:
            player1.attackByGhost()
        elif rand == 4:
            player1.increaseFloor()
        elif rand == 5:
            player1.fallInHole()
        elif rand == 6:
            player1.goblinStolePotion()
        elif rand == 7:
            player1.decreaseFloor()

    def choose_method_2(self, rand):
        if rand == 1:
            player2.increasePotion()
        elif rand == 2:
            player2.stubbedToe()
        elif rand == 3:
            player2.attackByGhost()
        elif rand == 4:
            player2.increaseFloor()
        elif rand == 5:
            player2.fallInHole()
        elif rand == 6:
            player2.goblinStolePotion()
        elif rand == 7:
            player2.decreaseFloor()

print("Welcome to the RPG Dungeon Crawler!")
print("Your goal is to go deep into the dungeon without dying.")
print("Controls are simple, use 'WASD' to move up, left, down, and right respectively.")
print("Press 'E' to use any potions in your inventory to gain health.")
print("Good Luck!")
print('     W     ')
print('A    S    D')
print('Press E to use potion.')

player1Check = playerCheck()
player2Check = playerCheck()
player1_turn = 0
player2_turn = 0

random_int = 1
guess = random.randint(0, 1000)
while int(player1.getHealth()) > 0 or int(player2.getHealth()) > 0:
    while int(player1.getHealth()) > 0:
        player1_turn += 1
        print('\n')
        print(player1_name, ':', player1.getHealth())
        print("Potion count: ", player1.getPotions())
        print("Level :", player1.getLevel())
        key_press = str(input("Player 1, choose your next direction"))
        if key_press == 'w':
            print('You moved forward.')
            rand_value = random.randint(1, 4)
            for i in range(rand_value):
                random_single = random.randint(1, 8)
                angel_value = random.randint(1, 1000)
                player1Check.choose_method_1(random_single)
                player1.setHealth(player1Check.check_health(player1, player1.getHealth()))
                player1.setPotion(player1Check.check_potion(player1.getPotions()))
                player1Check.rand_funct(angel_value, guess)
                print('\n')

            break
        elif key_press == 'a':
            print('You moved left.')
            rand_value = random.randint(1, 4)
            for i in range(rand_value):
                random_single = random.randint(1, 8)
                angel_value = random.randint(1, 1000)
                player1Check.choose_method_1(random_single)
                player1.setHealth(player1Check.check_health(player1, player1.getHealth()))
                player1.setPotion(player1Check.check_potion(player1.getPotions()))
                player1Check.rand_funct(angel_value, guess)
                print('\n')

            break
        elif key_press == 's':
            print('You moved backwards.')
            rand_value = random.randint(1, 4)
            for i in range(rand_value):
                random_single = random.randint(1, 8)
                angel_value = random.randint(1, 1000)
                player1Check.choose_method_1(random_single)
                player1.setHealth(player1Check.check_health(player1, player1.getHealth()))
                player1.setPotion(player1Check.check_potion(player1.getPotions()))
                player1Check.rand_funct(angel_value, guess)
                print('\n')

            break
        elif key_press == 'd':
            print('You moved right.')
            rand_value = random.randint(1, 4)
            for i in range(rand_value):
                random_single = random.randint(1, 8)
                angel_value = random.randint(1, 1000)
                player1Check.choose_method_1(random_single)
                player1.setHealth(player1Check.check_health(player1, player1.getHealth()))
                player1.setPotion(player1Check.check_potion(player1.getPotions()))
                player1Check.rand_funct(angel_value, guess)
                print('\n')

            break
        elif key_press == 'e':
            player1.usePotion()

        break

    while int(player2.getHealth()) > 0:
        player2_turn += 1
        print('\n')
        print(player2_name, ':', player2.getHealth())
        print("Potion count: ", player2.getPotions())
        print("Level :", player2.getLevel())
        key_press = str(input("Player 2, choose your next direction"))
        if key_press == 'w':
            print('\n')
            print('You moved forward.')
            rand_value = random.randint(1, 4)
            for i in range(rand_value):
                random_single = random.randint(1, 8)
                angel_value = random.randint(1, 1000)
                player2Check.choose_method_2(random_single)
                player2.setHealth(player2Check.check_health(player2, player2.getHealth()))
                player2.setPotion(player2Check.check_potion(player2.getPotions()))
                player2Check.rand_funct(angel_value, guess)
                print('\n')

            break
        elif key_press == 'a':
            print('You moved left.')
            rand_value = random.randint(1, 4)
            for i in range(rand_value):
                random_single = random.randint(1, 8)
                angel_value = random.randint(1, 1000)
                player2Check.choose_method_2(random_single)
                player2.setHealth(player2Check.check_health(player2, player2.getHealth()))
                player2.setPotion(player2Check.check_potion(player2.getPotions()))
                player2Check.rand_funct(angel_value, guess)
                print('\n')

            break
        elif key_press == 's':
            print('You moved backwards.')
            rand_value = random.randint(1, 4)
            for i in range(rand_value):
                random_single = random.randint(1, 8)
                angel_value = random.randint(1, 1000)
                player2Check.choose_method_2(random_single)
                player2.setHealth(player2Check.check_health(player2, player2.getHealth()))
                player2.setPotion(player2Check.check_potion(player2.getPotions()))
                player2Check.rand_funct(angel_value, guess)
                print('\n')

            break
        elif key_press == 'd':
            print('You moved right.')
            rand_value = random.randint(1, 4)
            for i in range(rand_value):
                random_single = random.randint(1, 8)
                angel_value = random.randint(1, 1000)
                player2Check.choose_method_2(random_single)
                player2.setHealth(player2Check.check_health(player2, player2.getHealth()))
                player2.setPotion(player2Check.check_potion(player2.getPotions()))
                player2Check.rand_funct(angel_value, guess)
                print('\n')

            break
        elif key_press == 'e':
            player2.usePotion()

        break


if int(player1.getHealth()) <= 0 and int(player2.getHealth()) <= 0:
    newFile = open('RPG.txt', 'r+')
    newFile.write('Player name: ')
    newFile.write(str(player1.getPlayerName()))
    newFile.write('\n')
    newFile.write('Level: ')
    newFile.write(str(player1.getLevel()))
    newFile.write('\n')
    newFile.write('Potions: ')
    newFile.write(str(player1.getPotions()))
    newFile.write('\n')
    newFile.write('Turns: ')
    newFile.write(str(player1_turn))
    newFile.write('\n')
    newFile.write('\n')
    newFile.write('Player name: ')
    newFile.write(str(player2.getPlayerName()))
    newFile.write('\n')
    newFile.write('Level: ')
    newFile.write(str(player2.getLevel()))
    newFile.write('\n')
    newFile.write('Potions: ')
    newFile.write(str(player2.getPotions()))
    newFile.write('\n')
    newFile.write('Turns: ')
    newFile.write(str(player2_turn))
    newFile.write('\n')
else:
    pass


