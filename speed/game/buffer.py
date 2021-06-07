from game.actor import Actor
from game.point import Point

class Buffer(Actor):

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        super().__init__()
        self.buffer = ""
        position = Point(1,20)
        self.set_position(position)
        self.set_text(f"Buffer: {self.buffer}")

    def update_buffer(self, word):
        """Update the buffer.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        if word == "*":
            self.clear_buffer()
        else:
            self.buffer += str(word)
            self.set_text(f"Buffer: {self.buffer}")

    def clear_buffer(self):
        """Clear the buffer.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        self.buffer = ""
        self.set_text(f"Buffer: {self.buffer}")

    def get_buffer(self):
        return self.buffer # Return string
