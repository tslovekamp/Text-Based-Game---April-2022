#program header
'''Name: Tyler Lovekamp
   Date: 4/20/2022
   Assignment: Final Project
   Pseudocode: (when needed)
'''

#Patch Notes
'''
4/20/22
Created Actions File
'''
import os
class Actions():
    #Variables
    _level = 0
    _health = 100
    _potions = 0
    _playerName = ''
    _guardianAngel = 0
    #Constructor
    def __init__(self):
        self._level = 0
        self._health = 100
        self._potions = 0
        self._playerName = ''
        self._guardianAngel = 0
        self._newFile = open('RPG.txt', 'w')
    #Getters/Setters
    def getHealth(self):
        return self._health
    def getLevel(self):
        return self._level
    def getPotions(self):
        return self._potions
    def getPlayerName(self):
        return self._playerName
    def setPlayerName(self, playerName):
        self._playerName = playerName
    def setLevel(self,level):
        self._level = level
    def setHealth(self, health):
        self._health = health
    def setPotion(self, potion):
        self._potions = potion
    #Behaviors
    def increasePotion(self):
        self._potions = self._potions + 1
        print('You found a potion!')
        

    def usePotion(self):
        if (self._potions) >= 1:
            self._potions = self._potions - 1
            self._health = self._health + 50
            print('You used a potion, + 50 health')
        else:
            print('You have no potions to use!')
       

    def stubbedToe(self):
        self._health = self._health - 5
        print('You stubbed your toe, - 5 health')
        

    def attackByGhost(self):
        self._health = self._health - 20
        print('You encountered a Ghost who attacked you, - 20 health')
        

    def increaseFloor(self):
        self._floor = self._level + 1
        print('You found the stairs to the next floor')
        

    def fallInHole(self):
        self._level = self._level + 3
        self._health = self._health - 50
        print('You fell in a hole and lost 50 health but gained 3 floors')
        

    def goblinStolePotion(self):
        if self._potions<=0:
            self._potions = 0
            print("You encountered a goblin who wanted to steal a potion, but found none to steal.")
            print("The goblin proceeded to mock you for having no potions.")
        else:
            self._potions = self._potions - 1
            print('You encountered a goblin who stole a potion, - 1 potion')
        

    def decreaseFloor(self):
        self._level = self._level - 2
        if self._level <=0:
            self._level = 0
            print("You wandered off and found a ladder and returned to the starting floor.")
        else:
            print('You wandered off and found a ladder and went up 2 floors')
        

    def foundBasilisk(self):
        self._health = 0
        print('You found a Basilisk and it killed you with a single stare')

    def foundGuardianAngel(self):
        self._guardianAngel = self._guardianAngel + 1
        print('You found a Guardian Angel that will protect you on your next death')

    def useGuardianAngel(self):
        self._guardianAngel = self._guardianAngel - 1
        self._health = 100
        print('Your Guardian Angel saved you from imminent death!')

    def openFile(self):
        self._newFile = open('RPG.txt', 'r+')

    def saveInfoToText(self, turn):
        self._newFile.write('Player Name: ')
        self._newFile.write(str(self._playerName))
        self._newFile.write('\n')
        self._newFile.write('Level: ')
        self._newFile.write(str(self._level))
        self._newFile.write('\n')
        self._newFile.write('Potions: ')
        self._newFile.write(str(self._potions))
        self._newFile.write('\n')
        self._newFile.write('Turns: ')
        self._newFile.write(str(turn))

    def readFromFile(self):
        self._newFile = open('RPG.txt', 'r')
        llist = self._newFile.readlines()
        for item in llist:
            print(item)
        self._newFile.close()

    def closeFile(self):
        self._newFile.close()
