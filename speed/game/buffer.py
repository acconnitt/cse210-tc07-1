from game.actor import Actor
from game.point import Point

class Buffer(Actor):

    def __init__(self):
        super().__init__()
        self.buffer = ""
        position = Point(1,20)
        self.set_position(position)
        self.set_text(f"Buffer: {self.buffer}")

    def update_buffer(self, word):
        self.buffer += str(word)
        self.set_text(f"Buffer: {self.buffer}")

    def clear_buffer(self):
        self.buffer = ""
        self.set_text(f"Buffer: {self.buffer}")

    def get_buffer(self):
        return self.buffer
