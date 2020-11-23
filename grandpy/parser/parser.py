"""
Parser module
"""
from re import sub, split


from configuration.config import STOPWORDS, KEYWORDS
from grandpy.parser.word import Word

class Parser:
    """
    """
    def __init__(self, question):
        self.question = question
        self.words_list = None
        self.stop_words_list = STOPWORDS
        self.key_words_list = KEYWORDS
        self.word_list = []
        self.keyword_present = False
        self.start_word_index = None
        self.end_word_index = None
        self.parsed_string = ""
        self.split_question()
        self.lower_lists()
        self.create_word()
        self.enumerate_word()
        self.get_next_word_enumeration()
        self.find_start_word_position()
        self.find_end_word_position()
        self.generate_parsed_string()

    def split_question(self):
        """
        """
        self.question = self.question.strip(" ,.?!")
        self.question = sub("[,.?!']"," ", self.question)
        while "  " in self.question:
            self.question = self.question.replace("  "," ")
        self.words_list = split(" ",self.question)


    def lower_lists(self):
        """
        """
        self.words_list = [question_word.lower() for question_word
                in self.words_list]
        self.stop_words_list = [stop_word.lower() for
                stop_word in self.stop_words_list]
        self.key_words_list = [stop_word.lower() for
                stop_word in self.key_words_list]

    def create_word(self):
        counter = 0
        for word_in_list in self.words_list:
            word = Word()
            word.index = counter
            word.name = word_in_list
            self.word_list.append(word)
            counter += 1

    def enumerate_word(self):
        """
        """
        for word in self.word_list:
            word.enumeration = "1"
            for stop_word in self.stop_words_list:
                if word.name == stop_word:
                    word.enumeration = "0"
            for key_word in self.key_words_list:
                if word.name == key_word:
                    word.enumeration = "2"

    def get_next_word_enumeration(self):
        """
        """
        list_len = len(self.word_list)
        for word in self.word_list:
            counter = 1
            if word.index != 0: 
                enumeration_value = [next_word.enumeration for\
                        next_word in self.word_list if\
                        word.index - 1 == next_word.index]
                word.word_minus_one_enumeration = enumeration_value[0]
            if counter <= list_len - 1:
                for word_plus_one in self.word_list:
                    if word_plus_one.index == word.index + 1:
                        word.word_plus_one_enumeration = \
                                word_plus_one.enumeration
            if counter <= list_len - 2:
                for word_plus_two in self.word_list:
                    if word_plus_two.index == word.index + 2:
                        word.word_plus_two_enumeration = \
                                word_plus_two.enumeration

    def find_start_word_position(self):
        """
        """
        for word in self.word_list:
            if word.enumeration == "2":
                self.keyword_present = True
        starts_analysis = False
        for word in self.word_list:
            if self.keyword_present:
                if word.enumeration == "2":
                    starts_analysis = True
                if starts_analysis and word.enumeration == "1":
                    self.start_word_index = word.index
                    starts_analysis = False
            else:
                if word.enumeration == "1":
                    self.start_word_index = word.index

    def find_end_word_position(self):
        """
        """
        continue_analysis = True
        for word in self.word_list:
            if word.index >= self.start_word_index and\
                    continue_analysis: 
                if word.enumeration == "1" and \
                        word.word_plus_one_enumeration== "0" and\
                        word.word_plus_two_enumeration == "0":
                    self.end_word_index = word.index
                    continue_analysis = False
                elif word.enumeration == "1" and \
                        word.word_plus_one_enumeration == "0" and\
                        word.word_plus_two_enumeration == None:
                    self.end_word_index = word.index
                    continue_analysis = False
                elif word.enumeration== "1" and \
                        word.word_plus_one_enumeration == None and\
                        word.word_plus_two_enumeration == None:
                    self.end_word_index = word.index
                    continue_analysis = False

    def generate_parsed_string(self):
        """
        """
        parsed_list = []
        for word in self.word_list:
            if word.index >= self.start_word_index and \
                    word.index <= self.end_word_index:
                parsed_list.append(word.name)
        counter = 1
        for word in parsed_list:
            if counter < len(parsed_list):
                self.parsed_string += str(word)
                self.parsed_string += str(" ")
                counter += 1
            else:
                self.parsed_string += str(word)
        print(self.parsed_string)
