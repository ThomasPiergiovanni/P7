"""Parser module
"""
from re import sub, split

from configuration.config import STOPWORDS, KEYWORDS
from grandpy.parser.word import Word


class Parser:
    """Parser class
    """
    def __init__(self):
        self.stop_words_list = STOPWORDS
        self.key_words_list = KEYWORDS
        self.question = ""
        self.word_instances_list = []
        self.boundaries_index = {
                "start": 0, "end": 0}
        self.parsed_chain = ""
        self.status = False

    def parse(self):
        """Method that performs the entire parsin action on the user
        question.
        """
        self.normalize_question()
        self.lower_lists()
        self.create_word()
        self.enumerate_word()
        self.enumerate_nexts_words()
        self.start_position()
        self.end_position()
        self.generate_parsed_chain()

    def normalize_question(self):
        """Method that normalize the user question and make a list of
        word out of it.
        """
        self.question = self.question.strip(" ,.?!")
        self.question = sub("[,.?!']", " ", self.question)
        while "  " in self.question:
            self.question = self.question.replace("  ", " ")
        self.question = split(" ", self.question)

    def lower_lists(self):
        """Method lowers user question but also the
        stop word and key word list.
        """
        self.question = [
                question_word.lower() for question_word in self.question]
        self.stop_words_list = [
                stop_word.lower() for stop_word in self.stop_words_list]
        self.key_words_list = [
                stop_word.lower() for stop_word in self.key_words_list]

    def create_word(self):
        """Method creating Word instances and put them into a list.
        """
        counter = 0
        for word_in_list in self.question:
            word = Word()
            word.index = counter
            word.name = word_in_list
            self.word_instances_list.append(word)
            counter += 1

    def enumerate_word(self):
        """Method creating word enumeration based on the stop word and key
        word list i.e. it codes a word into a numeric value.
        """
        for word in self.word_instances_list:
            word.enum["self"] = "1"
            for stop_word in self.stop_words_list:
                if word.name == stop_word:
                    word.enum["self"] = "0"
            for key_word in self.key_words_list:
                if word.name == key_word:
                    word.enum["self"] = "2"

    def enumerate_nexts_words(self):
        """Method that, for a given word, gets the words enumerations values
        of the nexts words i.e. the two words places before in the list
         the three words places after in the list.
        """
        list_len = len(self.word_instances_list)
        for word in self.word_instances_list:
            counter = 1
            if word.index != 0:
                enum_value = [
                        next_word.enum["self"] for next_word in
                        self.word_instances_list if word.index - 1 ==
                        next_word.index]
                word.enum["min_one"] = enum_value[0]
            if word.index != 0 and word.index != 1:
                enum_value = [
                        next_word.enum["self"] for next_word in
                        self.word_instances_list if word.index - 2 ==
                        next_word.index]
                word.enum["min_two"] = enum_value[0]
            if counter <= list_len - 1:
                for word_plus_one in self.word_instances_list:
                    if word_plus_one.index == word.index + 1:
                        word.enum["plus_one"] = word_plus_one.enum["self"]
            if counter <= list_len - 2:
                for word_plus_two in self.word_instances_list:
                    if word_plus_two.index == word.index + 2:
                        word.enum["plus_two"] = word_plus_two.enum["self"]
            if counter <= list_len - 3:
                for word_plus_three in self.word_instances_list:
                    if word_plus_three.index == word.index + 3:
                        word.enum["plus_three"] = word_plus_three.enum["self"]

    def start_position(self):
        """Method that define which word is the starting word in the list for
        creating the parsed chain i.e. the word(s) chain to send to the
        different APIs.
        """
        keyword_present = False
        for word in self.word_instances_list:
            if word.enum["self"] == "2":
                keyword_present = True
        starts_analysis = False
        for word in self.word_instances_list:
            if keyword_present:
                if word.enum["self"] == "2":
                    starts_analysis = True
                if starts_analysis and word.enum["self"] == "1":
                    self.boundaries_index["start"] = word.index
                    starts_analysis = False
            else:
                if (
                            word.enum["self"] == "1" and
                            word.enum["plus_one"] is not None and
                            word.enum["plus_two"] is not None and
                            word.enum["plus_three"] is None):
                    self.boundaries_index["start"] = word.index
                elif (
                            word.enum["self"] == "1" and
                            word.enum["min_one"] != "1" and
                            word.enum["plus_one"] is not None and
                            word.enum["plus_two"] is None):
                    self.boundaries_index["start"] = word.index
                elif (
                            word.enum["self"] == "1" and
                            word.enum["min_two"] != "1" and
                            word.enum["min_one"] != "1" and
                            word.enum["plus_one"] is None):
                    self.boundaries_index["start"] = word.index

    def end_position(self):
        """Method that define which word is the ending word in the list for
        creating the parsed chain i.e. the word(s) chain to send to the
        Google Place API
        """
        continue_analysis = True
        for word in self.word_instances_list:
            if word.index >= self.boundaries_index["start"] and\
                    continue_analysis:
                if (
                        word.enum["self"] == "1" and
                        word.enum["plus_one"] is None and
                        word.enum["plus_two"] is None):
                    self.boundaries_index["end"] = word.index
                    continue_analysis = False
                elif (
                        word.enum["self"] == "1" and
                        word.enum["plus_one"] == "0" and
                        word.enum["plus_two"] is None):
                    self.boundaries_index["end"] = word.index
                    continue_analysis = False
                elif (
                        word.enum["self"] == "1" and
                        word.enum["plus_one"] == "0" and
                        word.enum["plus_two"] == "0"):
                    self.boundaries_index["end"] = word.index
                    continue_analysis = False

    def generate_parsed_chain(self):
        """ Method that create the word chain to send to the Google
        Place API.
        """
        parsed_list = []
        for word in self.word_instances_list:
            if (
                    word.index >= self.boundaries_index["start"] and
                    word.index <= self.boundaries_index["end"]):
                parsed_list.append(word.name)
        if len(parsed_list) != 0:
            self.status = True
            counter = 1
            for word in parsed_list:
                if counter < len(parsed_list):
                    self.parsed_chain += str(word)
                    self.parsed_chain += str(" ")
                    counter += 1
                else:
                    self.parsed_chain += str(word)
