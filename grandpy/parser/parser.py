"""
Parser module
"""
from re import sub, split


from configuration.config import STOPWORDS, KEYWORDS
from grandpy.parser.word import Word

class Parser:
    """
    """
    def __init__(self):
        self.stop_words_list = STOPWORDS
        self.key_words_list = KEYWORDS
        self.question = ""
        self.question_strip = ""
        self.words_list = None
        self.word_instances_list = []
        self.keyword_present = False
        self.start_index = 0
        self.end_index = 0
        self.parsed_string = ""

    def parse(self):
        self.split_question()
        self.lower_lists()
        self.create_word()
        self.enumerate_word()
        self.enumerate_nexts()
        self.start_position()
        self.end_position()
        self.generate_parsed_string()

    def split_question(self):
        """
        """
        self.question_strip = self.question.strip(" ,.?!")
        self.question_strip = sub("[,.?!']"," ", self.question_strip)
        while "  " in self.question_strip:
            self.question_strip = self.question_strip.replace("  "," ")
        self.words_list = split(" ",self.question_strip)


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
            self.word_instances_list.append(word)
            counter += 1

    def enumerate_word(self):
        """
        """
        for word in self.word_instances_list:
            word.enum = "1"
            for stop_word in self.stop_words_list:
                if word.name == stop_word:
                    word.enum = "0"
            for key_word in self.key_words_list:
                if word.name == key_word:
                    word.enum = "2"

    def enumerate_nexts_words(self):
        """
        """
        list_len = len(self.word_instances_list)
        for word in self.word_instances_list:
            counter = 1
            if word.index != 0: 
                enum_value = [next_word.enum for\
                        next_word in self.word_instances_list if\
                        word.index - 1 == next_word.index]
                word.min_one_enum = enum_value[0]
            if word.index != 0 and word.index != 1: 
                enum_value = [next_word.enum for\
                        next_word in self.word_instances_list if\
                        word.index - 2 == next_word.index]
                word.min_two_enum = enum_value[0]
            if counter <= list_len - 1:
                for word_plus_one in self.word_instances_list:
                    if word_plus_one.index == word.index + 1:
                        word.plus_one_enum = \
                                word_plus_one.enum
            if counter <= list_len - 2:
                for word_plus_two in self.word_instances_list:
                    if word_plus_two.index == word.index + 2:
                        word.plus_two_enum = \
                                word_plus_two.enum

    def start_position(self):
        """
        """
        for word in self.word_instances_list:
            if word.enum == "2":
                self.keyword_present = True
        starts_analysis = False
        for word in self.word_instances_list:
            if self.keyword_present:
                if word.enum == "2":
                    starts_analysis = True
                if starts_analysis and word.enum == "1":
                    self.start_index = word.index
                    starts_analysis = False
            else:
                if word.enum == "1" and\
                        word.min_two_enum != 1 and\
                        word.plus_one_enum == None:
                    self.start_index = word.index
                elif word.enum == "1" and\
                        word.min_two_enum != 1 and\
                        word.plus_two_enum == None:
                    self.start_index = word.index
                else:
                    if word.enum == "1":
                        self.start_index = word.index

    def end_position(self):
        """
        """
        continue_analysis = True
        for word in self.word_instances_list:
            if word.index >= self.start_index and\
                    continue_analysis: 
                if word.enum == "1" and \
                        word.plus_one_enum== "0" and\
                        word.plus_two_enum == "0":
                    self.end_index = word.index
                    continue_analysis = False
                elif word.enum == "1" and \
                        word.plus_one_enum == "0" and\
                        word.plus_two_enum == None:
                    self.end_index = word.index
                    continue_analysis = False
                elif word.enum== "1" and \
                        word.plus_one_enum == None and\
                        word.plus_two_enum == None:
                    self.end_index = word.index
                    continue_analysis = False


    def generate_parsed_string(self):
        """
        """
        parsed_list = []
        for word in self.word_instances_list:
            if word.index >= self.start_index and \
                    word.index <= self.end_index:
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
