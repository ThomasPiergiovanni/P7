"""
Survey module
"""
from re import split, escape


from grandpy.configuration.config import STOPWORDS


class Survey:
    """
    """
    def __init__(self):
        self.question_label = "Ask your question here: \n"
        self.question = None
        self.parsing_list = []
        self.normalized_question_word_list = []
        self.normalized_stop_words_list = []
        self.filtered_list = []
        self.address_answer = None
        self.random_info_answer = None

    def ask_question(self):
        """
        """
        self.question = input(self.question_label)

    def split_question(self):
        """
        """
        self.question = "Quelle est l'adresse de l'Elysée"
        self.my_delimiters = " ", "'"
        self.regular_expression = '|'.join(map(escape, self.my_delimiters)) 
        self.split_list = split(self.regular_expression, self.question)
        # print(self.split_list)

    def normalize_lists(self):
        for question_word in self.split_list:
            self.normalized_question_word_list.append(question_word.lower())
        for stop_word in STOPWORDS:
            self.normalized_stop_words_list.append(stop_word.lower())
        
        # print(self.normalized_question_word_list)
        # print(self.normalized_stop_words_list)

    def filter_list(self):
        for question_word in self.normalized_question_word_list:
            for stop_word in STOPWORDS:
                if question_word == stop_word:
                    self.normalized_question_word_list.remove(question_word)

        print(self.normalized_question_word_list)
