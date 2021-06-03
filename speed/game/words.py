import random
from game.actor import Actor
from game.point import Point

class Words(Actor):
    """
    The Words class puts the words in the words.txt file into a list and returns a word from that list.
    """

    def __init__(self):
        super().__init__()
        self.words = []
        self.next_word = ""
        self.generate_list()
        self.set_text(self.get_next_word())
        self.set_position(Point(20, 3))
        self.move_next()

    def move_head(self, direction):
        """Moves the snake in the given direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        self.next_word.set_velocity(direction)
        word = se;f
        for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(direction)
            else:
                segment.set_velocity(direction)
            segment.move_next()

    def generate_list(self):
        words = open("game/words.txt", "r")
        for word in words:
            self.words.append(word)

        words.close()

    def get_next_word(self):
        self.next_word = self.words[random.randint(0,9999)]
        return self.next_word
