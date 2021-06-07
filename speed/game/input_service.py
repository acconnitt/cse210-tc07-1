import sys
from asciimatics.event import KeyboardEvent
import keyboard

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen

    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = self._screen.get_key()
        if not event is None:
            if keyboard.is_pressed('escape'):
                # This exits the code when escape is pressed.
                sys.exit()
            elif keyboard.is_pressed('enter'): 
                # This returns asterisk when enter is pressed.
                result = "*"
            elif event >= 97 and event <= 122:
                # This makes the result whatever letter is pressed. 
                result = chr(event)
        return result 
