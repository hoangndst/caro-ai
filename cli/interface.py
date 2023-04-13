import os
import lib.utils as utils
import lib.config as cfg

N = cfg.N

class GameUI(object):
    def __init__(self, ai):
        self.ai = ai

    def drawMenu(self): 
        print("Choose your color, 0 for black, 1 for white: ")  

    # Check which color the player has chosen
    def checkColorChoice(self, color):
        if color == 0:
            print("You choose black!")
            self.ai.turn = -1

        elif color == 1:
            print("You choose white!")
            self.ai.turn = 1
        
    def drawResult(self, tie=False):
        if tie:
            print("It's a TIE!")
            
        else:
            text = 'The winner is: '
            winner = self.ai.getWinner()
            print(text + winner)
