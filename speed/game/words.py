import random
from game.actor import Actor
from game.point import Point


class Words(Actor):
    """
    The Words class puts the words in the words.txt file into a list and returns a word from that list.
    """

    def __init__(self, word, y_value):
        """The class constructor.

        Args:
            self (Words): an instance of Words.
        """
        super().__init__()  # Inheritance
        self.set_text(word)  # An instance of Actor, a string as parameter
        # Set a position using ramdom
        self.set_position(Point(random.randint(1, 60), y_value))
        self.move_next()  # Moves the actor to its next position according to its velocity

    def move_head(self, direction):  # Funtion that updates the actor's velocity to the given one
        self.set_velocity(direction)  # The given velocity.
        self.move_next()

    def _get_text(self):  # An instance of Actor.
        return self.get_text()  # Returns a string

    def _get_position(self):  # An instance of Actor.
        return self.get_position()  # Returns the position.
