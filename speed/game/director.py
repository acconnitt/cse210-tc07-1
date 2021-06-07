from time import sleep
from game import constants
from game.words import Words
from game.score import Score
from game.point import Point
from game.buffer import Buffer
import random


class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        buffer (Buffer): The area that holds and displays the user input.
        words_list (Words): The words that move across the screen.
        generate_list = 
        input_service (InputService): The input mechanism.
        keep_playing (boolean): While True game continues.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.

    """

    def __init__(self, input_service, output_service):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._buffer = Buffer()
        self._word_list = []
        self.generate_list()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def generate_list(self):
        """Generates a list of words.

        Args:
            self (Director): an instance of Director.
        """
        positions = [2, 4, 6, 8, 10]

        # Words possitions
        for position in positions:
            # Choose ramdom words
            next_word = random.choice(constants.LIBRARY)
            # Append word to list
            self._word_list.append(Words(next_word, position))

    def _get_inputs(self):
        """Gets inputs.

        Args:
            self (Director): an instance of Director.
        """
        self._buffer.update_buffer(self._input_service.get_letter())
        direction = Point(1, 0)
        for word in self._word_list:
            word.move_head(direction)

    def _do_updates(self):
        """Do updates.

        Args:
            self (Director): an instance of Director.
        """
        for word in self._word_list:
            substring = word._get_text()
            if substring in self._buffer.get_buffer():
                position = word._get_position()
                self._score.add_points(len(substring))
                self._word_list.remove(word)
                next_word = random.choice(constants.LIBRARY)
                self._word_list.append(Words(next_word, position.get_y()))

    def _do_outputs(self):
        """Do ouputs.

        Args:
            self (Director): an instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actors(self._word_list)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()
