from time import sleep
from game import constants
from game.words import Words
from game.score import Score
from game.point import Point
from game.buffer import Buffer
import random


class Director:

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
        self.allwords = []
        
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
        words = open("game/words.txt", "r")
        list = []
        positions = [1, 3, 5, 7, 9]
        for word in words:
            list.append(word)
        position = 0
        self.allwords = list
        for position in positions:
            next_word = self.allwords[random.randint(0,9999)]
            position += 1
            self._word_list.append(Words(next_word, position))

        words.close()


    def _get_inputs(self):
        self._buffer.update_buffer(self._input_service.get_letter())
        direction = Point(1,0)
        for word in self._word_list:
            word.move_head(direction)


    def _do_updates(self):
        buffer = self._buffer.get_buffer()
        for word in self._word_list:
            substring = str(word)
            if substring in buffer:
                position = word.get_position()
                self._score.add_points(len(word))
                self._word_list.remove(word)
                next_word = self.allwords[random.randint(0,9999)]
                self._word_list.append(Words(next_word, position))


                
    def _do_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actors(self._word_list)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()
