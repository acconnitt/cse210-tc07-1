from time import sleep
from game import constants
from game.words import Words
from game.score import Score
from game.point import Point
from game.buffer import Buffer
import random
# from game.snake import Snake

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
        # self._snake = Snake()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._buffer.update_buffer(self._input_service.get_letter())
            if self._input_service.get_letter() == "*":
                self._buffer.clear_buffer()
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
        for position in positions:
            next_word = list[random.randint(0,9999)]
            position += 1
            self._word_list.append(Words(next_word, position))

        words.close()


    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.
        Args:
            self (Director): An instance of Director.
        """
        # direction = self._input_service.get_direction()
        direction = Point(1,0)
        for word in self._word_list:
            word.move_head(direction)
        self._input_service.get_letter()

        #self._buffer.update_buffer(self._input_service.get_letter())

        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.
        Args:
            self (Director): An instance of Director.
        """
        #self._handle_body_collision()
        #self._handle_food_collision()
        
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.
        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actors(self._word_list)
        #self._output_service.draw_actors(self._snake.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()
