# Game file

import random
from Input import InputManager
from enum import Enum

# Enum for validating game states
class GameState(Enum):
    GAME_RUNNING = 0
    GAME_OVER = 1

class Game:
    # Private fields
    __numbersolution : int
    __numberguesses: int
    __gamestate: GameState
    __number_buffer : list

    # Multi-line welcome message
    __game_message : str = """
        Lets play a little game shall we?
        I will select a 4 digit number...

        You will have to guess what number I have in mind

        for every digit you got right I will respond with Chicken
        for every digit you got wrong I will respond with Egg

        Lets see in how many guesses you can win

        Let's start!
    """

    # Constructor function
    # We will initialize the game-settings and values and display the welcome message
    def __init__(self):
        
        self.__numbersolution = random.randint(1000, 10000)
        self.__numberguesses = 0
        self.__gamestate = GameState.GAME_RUNNING
        self.__number_buffer = []

        self.__welcome_message()

    def __welcome_message(self) -> None:
        print(self.__game_message)
        print(self.__numbersolution)

    # Validate the input and check how many digits were right
    def __guess_number(self, guess : str) -> None:
        if (InputManager.isInt(guess) and InputManager.isFourDigit(guess)):

            amount_right = self.__right_amount(guess)
            amount_wrong = self.__wrong_amount(guess)

            print(f"{amount_right} chickens, {amount_wrong} eggs")
            self.__numberguesses += 1

    # See how many digits were correct
    def __right_amount(self, guess: str) -> int :
        right_amount : int = 0

        for index, value in enumerate(guess, start=0):
            if (value == str(self.__numbersolution)[index]):
                right_amount += 1

                self.__number_buffer.append(index)
        
        if (right_amount == 4) : self.__gamestate = GameState.GAME_OVER
        return right_amount

    # See how many digits were wrong
    def __wrong_amount(self, guess: str) -> int :
        wrong_amount : int = 0

        for index, value in enumerate(guess, start=0):
            if value in str(self.__numbersolution):
                if index not in self.__number_buffer:
                    wrong_amount += 1

        return wrong_amount

    # Start the game loop
    def startGame(self) -> None:
        while(self.__gamestate == GameState.GAME_RUNNING):
            user_input: str = input(f"Please choose a 4 digit number: ")

            self.__guess_number(user_input)

        print(f"Congrats you won! It took you {self.__numberguesses} tries to get it right")
