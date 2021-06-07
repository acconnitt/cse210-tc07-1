from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen


def main(screen):
    """ Class constructor
    """
    input_service = InputService(screen) # An instance of InputService 
    output_service = OutputService(screen) # An instance of OutputService
    director = Director(input_service, output_service) # An instance of Director.
    director.start_game() #An instance of Director.


Screen.wrapper(main) # Initialize the Screen
