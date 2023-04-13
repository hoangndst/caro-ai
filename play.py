from cli.interface import *
from lib.ai import *
import lib.utils as utils
import lib.gomoku as gomoku
import lib.config as cfg

N = cfg.N

def startGame():
    ai = GomokuAI()
    game = GameUI(ai)
    # # Draw the starting menu
    game.drawMenu()
    color = int(input())
    run = True
    while run:
        # Check which color the user has chosen and set the states
        game.checkColorChoice(color)
        if game.ai.turn == 1:
            game.ai.firstMove()
            game.ai.turn *= -1
                
        main(game)

        # When the game ends and there is a winner, draw the result board
        if game.ai.checkResult() != None:
            game.drawResult()
            print('Choose option: 0. Restart, 1. Quit')
            option = int(input())
            if option == 0:
                game.ai.turn = 0
                startGame()
            if option == 1:
                run = False
                break


### Main game play loop ###
def main(game):
    # pygame.init()
    end = False
    result = game.ai.checkResult()
    game.ai.drawBoard()
    while not end:
        turn = game.ai.turn

        # AI's turn
        if turn == 1:
            print('AI\'s turn')
            move_i, move_j = gomoku.ai_move(game.ai)
            # Make the move and update zobrist hash
            game.ai.setState(move_i, move_j, turn)
            game.ai.rollingHash ^= game.ai.zobristTable[move_i][move_j][0]
            game.ai.emptyCells -= 1

            result = game.ai.checkResult()
            # Switch turn
            game.ai.turn *= -1
            game.ai.drawBoard()

        # Human's turn
        if turn == -1:
            print('Your turn, enter your move: ')
            move = input() # move = i * N + j
            move_i = int(move) // N
            move_j = int(move) % N
            # Check the validity of human's move
            if game.ai.isValid(move_i, move_j):
                game.ai.boardValue = game.ai.evaluate(move_i, move_j, game.ai.boardValue, -1, game.ai.nextBound)
                game.ai.updateBound(move_i, move_j, game.ai.nextBound)
                game.ai.currentI, game.ai.currentJ = move_i, move_j
                # Make the move and update zobrist hash
                game.ai.setState(move_i, move_j, turn)
                game.ai.rollingHash ^= game.ai.zobristTable[move_i][move_j][1]
                game.ai.emptyCells -= 1                
                result =  game.ai.checkResult()
                game.ai.turn *= -1
                game.ai.drawBoard()
        if result != None:
            end = True
if __name__ == '__main__':
    startGame()