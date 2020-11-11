"""
Survey module
"""
from re import split, escape, search


from configuration.config import STOPWORDS


class Survey:
    """
    """
    def __init__(self):
        self.question_label = "Quelle est votre question?"
        self.question = None
        self.split_list = []
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
        self.my_delimiters = " ", "'"
        self.regular_expression = '|'.join(map(escape, self.my_delimiters)) 
        self.split_list = split(self.regular_expression, self.question)

    def normalize_lists(self):
        for question_word in self.split_list:
            self.normalized_question_word_list.append(question_word.lower())
        for stop_word in STOPWORDS:
            self.normalized_stop_words_list.append(stop_word.lower())
        
        # print(self.normalized_question_word_list)
        # print(self.normalized_stop_words_list)

    # def filter_list(self):
    #     for question_word in self.normalized_question_word_list:
    #         for stop_word in STOPWORDS:
    #             if question_word == stop_word:
    #                 self.normalized_question_word_list.remove(question_word)

    def write_pattern(self):
        split_lists = [
            ["où","se","trouve","la","tour","eiffel"],
            ["quelle","est","l","adresse","du","centre","commercial","de", "vélizy", "2"],
            ["où","se","trouve","l","arc","de","triomphe"],
            ["dis-moi","vieux","con","c","est","où","saint-Laurent-des-mortiers"]
            ]

        for split_list in split_lists:
            pattern = []
            for word_from_split in split_list:
                word_is_stopword = [word for word in STOPWORDS if word_from_split == word]
                if word_is_stopword:
                    pattern.append((0, word_from_split))
                else:
                    pattern.append((1,word_from_split))
            # print(split_list)
            print(pattern)
            # print(len(pattern))
            for elt in pattern:
                if elt[0] == 1 :
                    print(elt[1])
            del pattern
            print("-------")

    def regular_expression_start(self):
        pattern = "0011010101110"
        pattern_len = len(pattern) - 1
        reversed_pattern= pattern[::-1]

        # point de départ:
        start_1 = search(r"\b1", pattern)
        start_2 = search(r"\B1", pattern)
        end_1 = search(r"\B00", pattern)
        end_2 = search(r"\b1", reversed_pattern)
        end_3 = search(r"\B1", reversed_pattern)
        start_position = None
        end_position = None
        valid_word_present = True

        if start_1:
            start_position = start_1.start()
        elif start_2:
            start_position =  start_2.start()
        else:
            valid_word_present = False

        if end_1:
            end_position = end_1.start() - 1
        elif end_2:
            end_position = pattern_len - end_2.start()
        elif end_3:
            end_position = pattern_len - end_3.start()
        else:
            valid_word_present = False

        if valid_word_present:
            print ("Starts at index:",start_position,
            "\nEnds at index:", end_position )
        else:
            print("No word is valid")

    def regular_expression_end(self):
        pattern = "001101"

        result_1 = search(r"1\b", pattern)

        if result_1:
            print(result_1.span())



        # print(self.normalized_question_word_list)
