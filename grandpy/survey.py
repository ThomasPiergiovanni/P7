"""
Survey module
"""
from re import split, escape, search


from configuration.config import STOPWORDS, KEYWORDS


class Survey:
    """
    """
    def __init__(self):
        self.question_label = "Quelle est votre question?"
        self.question = None
        self.split_question_list = None
        self.stop_word_list = None

        self.prepared_questions_lists = []
        self.keyword_present = False



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

        
    def write_pattern(self):
        self.split_question_list = ["où","se","Trouve","l","arc","de","triomphe"]
        self.split_question_list = [question_word.lower() for question_word in self.split_question_list]

        # split_lists = [
        #     ["où","se","trouve","la","tour","eiffel"],
        #     ["quelle","est","l","adresse","du","centre","commercial","de", "vélizy", "2"],
        #     ["où","se","trouve","l","arc","de","triomphe"],
        #     ["dis-moi","vieux","con","c","est","où","saint-Laurent-des-mortiers"]
        #     ]

        # pattern =""

        #     for word_from_split in split_list:
        #         word_is_stopword = [word for word in STOPWORDS if word_from_split == word]
        #         word_is_keyword = [word for word in KEYWORDS if word_from_split == word]
        #         if word_is_keyword:
        #             pattern += str(2)                
        #         elif word_is_stopword:
        #             pattern += str(0)
        #         else:
        #             pattern += str(1)
        #             # pattern.append((1,word_from_split))
        #     self.self.prepared_questions_lists.append((split_list, pattern, 0))
        #     del pattern

    def find_keyword_position(self):
        pattern = "0211010101110"
        start_1 = search(r"\b2", pattern)
        start_2 = search(r"\B2", pattern)
        self.keyword_present = True


    def extract_querryable_pattern(self):

        if self.keyword_present:
            starts_collection = False
            for elt in pattern:
                if elt == "2" and starts_collection == False:
                    starts_collection = True
                elif starts_collection:
                    print(elt)

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


