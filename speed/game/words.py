import random
from game.actor import Actor
from game.point import Point

class Words(Actor):
    """
    The Words class puts the words in the words.txt file into a list and returns a word from that list.
    """

    def __init__(self, word, y_value):
        super().__init__()
        self.set_text(word)
        self.set_position(Point(random.randint(1,60), y_value))
        self.move_next()

    def move_head(self, direction):
        self.set_velocity(direction)
        self.move_next()
        
    def _get_text(self):
        return self.get_text()

    def _get_position(self):
        return self.get_position()
    
    