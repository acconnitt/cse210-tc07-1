class Buffer:

    def __init__(self):
        self.buffer = ""

    def update_buffer(self, word):
        self.buffer += str(word)

    def clear_buffer(self):
        self.buffer = ""

    def get_buffer(self):
        return self.buffer
