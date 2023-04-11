from abc import ABC, abstractmethod
from typing import Tuple, List, Union
import numpy as np

class BaseGame(ABC):
    """
    Base class for all games
    Two-player board game
    The game state should be represented in an immutable type for the MCTS
    (Monte Carlo Tree Search) process.
    The game state also needs to be converted into a form that can be fed to the
    Neural Network.
    """

    @property
    @abstractmethod
    def initial_state(self) -> int:
        """
        The initial state of the game in MCTS form. This is used in utils.play_game
        to start the MCTS loop.
        """
        pass

    @property
    @abstractmethod
    def obs_shape(self) -> Tuple[int, ...]:
        """
        The shape of the NN form of the game state.
        This is tuble of integers.
        Eg: [2, 3, 3]: 2 players x 3x3 board
        """
        pass
    
    @property
    @abstractmethod
    def action_space(self) -> int:
        """
        The total count of all possible actions that can be performed.
        This is a constant of each game that represents all actions,
        regardless of whether they are valid at each game state.
        
        Used to initialize MCTS nodes (determine how large the values, avg_values &
        visit count vectors are)

        Returns:
            (int): count of total possible actions
        """
        pass

    @abstractmethod
    def possible_moves(self, mcts_state: int) -> List:
        """
        Return List of all possible moves given game state
        
        Args:
            mcts_state (int): game state in MCTS form

        Return:
            List: List of possible actions
        """
        pass

    @abstractmethod
    def invalid_moves(self, mcts_state: int) -> List:
        """
        Return List of all invalid moves given game state
        
        Args:
            mcts_state (int): game state in MCTS form

        Return:
            List: List of invalid actions
        """
        pass

    @abstractmethod
    def states_to_training_batch(self, state_lists: List, who_moves_lists: List[int]) -> np.ndarray:
        """
        Convert game states into a form that can be used as training data for the NN.

        Args:
            state_lists (List): List of game states in MCTS form.
            who_moves_lists (List[int]): Corresponding list of player who made
                the move at that game state.

        Return:
            np.ndarray: For a 2 player game with board m x n, each game state
            will be represented as a 2 x m x n array. Each array will reflect the
            tokens/moves of one player with value 1 and have zero values in
            all other locations (opposing player's token and empty locations).
            This is how the data is fed to the neural network in the AlphaZero paper.
        """
        pass

    @abstractmethod
    def move(self, mcts_state: int, move: int, player: int) -> Tuple[int, bool]:
        """
        Given the current game state and a (legal) move by a player,
        get the new game state and whether or not the move led to a win. 

        Args:
            mcts_state (int): Game state in MCTS form
            move (int): Action performed
            player (int): Which of the 2 player (0 or 1) performed the action

        Returns:
            Tuple[int, bool]: New game state, whether the game had been won
                (by the player who made the move)
        """
    
    @abstractmethod
    def render(self, mcts_state: int) -> str:
        """
        Render a string representation of the current game state

        Args:
            mcts_state (int): Game state in MCTS form

        Returns:
            Union[str, List[str]]: String representation of game state
        """
        pass