"""
Survey module
"""
from re import split, escape, search


from configuration.config import STOPWORDS, KEYWORDS

class Word:
    def __init__(self):
        self.index = None
        self.name = None
        self.pattern = None
        self.selected = False
        self.start_position = False
        self.end_position = False

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
        self.parsed_question = ""



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
        self.split_question_list = [question_word.lower() for question_word in self.split_question_list]
        self.stop_word_list = [stop_word.lower() for stop_word in STOPWORDS]

        
    def define_pattern(self):
        self.split_question_list = ["où","se","Trouve","l","arc","de","triomphe"]
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
                word.pattern = "2"              
            elif word_is_stopword:
                word.name = word_from_split
                word.pattern = "0"
            else:
                word.name = word_from_split
                word.pattern = "1"

            self.words_list.append(word)
            counter += 1



    def regular_expression_start(self):

        starts_analysis = False
        starts_collection = False
        for word in self.words_list:
            if word.pattern == "2":
                starts_analysis = True
            if starts_analysis:
                word_minus_one_pattern = [next_word.pattern for next_word in self.words_list if word.index - 1 ==  next_word.index]
                word_plus_one_pattern = [next_word.pattern for next_word in self.words_list if word.index + 1 ==  next_word.index]
                if word.pattern == "1":
                    word.selected = "1"            
                elif word.pattern == "0" and word_plus_one_pattern[0] =="1" and word_minus_one_pattern[0] == "1":
                    word.selected = "1"
        
        parsed_list = []
        for word in self.words_list:
            if word.selected:
                parsed_list.append(word.name)

        counter = 1
        for word in parsed_list:
            if counter < len(parsed_list):
                self.parsed_question += str(word)
                self.parsed_question += str(" ")
                counter += 1
            else:
                self.parsed_question += str(word)

        print(self.parsed_question)

