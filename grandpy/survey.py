"""
Survey module
"""
from re import split, escape, search


from grandpy.configuration.config import STOPWORDS, KEYWORDS

class Word:
    def __init__(self):
        self.index = None
        self.name = None
        self.code = None
        self.word_minus_one_code = None
        self.word_plus_one_code = None
        self.word_plus_two_code = None

class Survey:
    """
    """
    def __init__(self):
        self.question_label = "Quelle est votre question?"
        self.question = None
        self.split_question_list = None
        self.stop_word_list = None
        self.words_list = []
        self.keyword_present = False
        self.start_word_index = None
        self.end_word_index = None
        self.parsed_string = ""

    def ask_question(self):
        """
        """
        self.question = input(self.question_label)

    def split_question(self):
        """
        """
        self.my_delimiters = " ", "'"
        self.regular_expression = '|'.join(map(escape, self.my_delimiters)) 
        self.split_question_list = split(self.regular_expression, self.question)

    def normalize_lists(self):
        """
        """
        self.split_question_list = [question_word.lower() for question_word in self.split_question_list]
        self.stop_word_list = [stop_word.lower() for stop_word in STOPWORDS]

    def define_word_code(self):
        self.split_question_list = ["quelle","est","l","adresse","du","centre","commercial","de", "vélizy", "2"]
        self.split_question_list = [question_word.lower() for question_word in self.split_question_list]



        # split_lists = [
        #     ["où","se","trouve","la","tour","eiffel"],
        #     ["quelle","est","l","adresse","du","centre","commercial","de", "vélizy", "2"],
        #     ["où","se","trouve","l","arc","de","triomphe"],
        #     ["dis-moi","vieux","con","c","est","où","saint-Laurent-des-mortiers"]
        #     ]
        counter = 0
        for word_from_split in self.split_question_list:
            word_is_stopword = [word for word in STOPWORDS if word_from_split == word]
            word_is_keyword = [word for word in KEYWORDS if word_from_split == word]
            word = Word()
            word.index = counter

            if word_is_keyword:
                word.name = word_from_split
                word.code = "2"              
            elif word_is_stopword:
                word.name = word_from_split
                word.code = "0"
            else:
                word.name = word_from_split
                word.code = "1"

            self.words_list.append(word)
            counter += 1


    def get_next_word_code(self):
        """
        """
        list_len = len(self.words_list)
        for word in self.words_list:
            counter = 1
            if word.index != 0: 
                code_value = [next_word.code for
                        next_word in self.words_list if word.index - 1 ==  next_word.index]
                word.word_minus_one_code = code_value[0]
            if counter <= list_len - 1:
                for word_plus_one in self.words_list:
                    if word_plus_one.index == word.index + 1:
                         word.word_plus_one_code = word_plus_one.code
            if counter <= list_len - 2:
                for word_plus_two in self.words_list:
                    if word_plus_two.index == word.index + 2:
                         word.word_plus_two_code = word_plus_two.code

    def find_start_word_position(self):
        """
        """
        for word in self.words_list:
            if word.code == "2":
                self.keyword_present = True

        starts_analysis = False
        for word in self.words_list:
            if self.keyword_present:
                if word.code == "2":
                    starts_analysis = True
                if starts_analysis and word.code == "1":
                    self.start_word_index = word.index
                    starts_analysis = False
            else:
                if word.code == "1":
                    self.start_word_index = word.index

    def find_end_word_position(self):
        """
        """
        continue_analysis = True
        for word in self.words_list:
            if word.index >= self.start_word_index and continue_analysis: 
                if word.code == "1" and \
                        word.word_plus_one_code == "0" and \
                        word.word_plus_two_code == "0":
                    self.end_word_index = word.index
                    continue_analysis = False

                elif word.code == "1" and \
                        word.word_plus_one_code == "0" and \
                        word.word_plus_two_code == None:
                    self.end_word_index = word.index
                    continue_analysis = False
 
                elif word.code == "1" and \
                        word.word_plus_one_code == None and word.word_plus_two_code == None:
                    self.end_word_index = word.index
                    continue_analysis = False


    def generate_parsed_string(self):
        """
        """
        parsed_list = []
        for word in self.words_list:
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
