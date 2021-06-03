import random
from game.actor import Actor
from game.point import Point

class Words(Actor):
    """
    The Words class puts the words in the words.txt file into a list and returns a word from that list.
    """

    def __init__(self, word, position):
        super().__init__()
        self.set_text(word)
        self.set_position(Point(random.randint(1,60), position))
        self.move_next()

    def move_head(self, direction):
        """Moves the snake in the given direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        
        self.set_velocity(direction)
        self.move_next()
        '''for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(direction)
            else:
                segment.set_velocity(direction)
            segment.move_next()'''

