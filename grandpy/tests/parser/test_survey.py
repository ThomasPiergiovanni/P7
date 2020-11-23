"""
"""
from grandpy.parser.parser import Parser

class TestParser:

    class MockWord:
        def __init__(self):
            self.index = None
            self.name = None
            self.enumeration = None
            self.word_minus_one_enumeration = None
            self.word_plus_one_enumeration = None
            self.word_plus_two_enumeration = None

    t_questions_list = [
        "Où se trouve la Tour Eiffel?", 
        "Quelle est l'adresse du Centre Commercial de Vélizy 2?",
        "Où se trouve l'Arc de Triomphe?",
        "Dis-moi vieux con! C'est ou Saint-Laurent-des-Mortiers?",
        "Ey toi, tu sais c'est où chez moi?"
        ]
    t_split_lists = [
        ["Où","se","trouve","la","Tour","Eiffel"],
        ["Quelle","est","l","adresse","du","Centre","Commercial","de", "Vélizy", "2"],
        ["Où","se","trouve","l","Arc","de","Triomphe"],
        ["Dis-moi","vieux","con","C","est","ou","Saint-Laurent-des-Mortiers"],
        ["Ey","toi","tu","sais","c","est","où","chez", "moi"]
        ]

    t_lowered_lists = [
        ["où","se","trouve","la","tour","eiffel"],
        ["quelle","est","l","adresse","du","centre","commercial","de", "vélizy", "2"],
        ["où","se","trouve","l","arc","de","triomphe"],
        ["dis-moi","vieux","con","c","est","ou","saint-laurent-des-mortiers"],
        ["ey","toi","tu","sais","c","est","où","chez", "moi"]
        ]

    tuple_list = [
        (0,"où","0",None,"0","2"),
        (1,"se","0","0","2","0"),
        (2,"trouve","2","0","0","1"),
        (3,"la","0","2","1","1"),
        (4,"tour","1","0","1",None),
        (5,"eiffel","1","1", None ,None)
        ]

    def test_ask_question(self, question, monkeypatch):
        t_parser = Parser()
        for question in self.t_questions_list:
            def mock_input(self):
                return question

            monkeypatch.setattr("builtins.input", mock_input)
            t_parser.ask_question()
            assert t_parser.question == question

    def test_split_question(self):
        t_parser = Parser()
        counter = 0 
        for question in self.t_questions_list:
            t_parser.question = question 
            t_parser.split_question()
            assert t_parser.words_list == self.t_split_lists[counter]
            counter += 1

    def test_lower_list(self):
        t_parser = Parser()
        counter = 0
        for question in self.t_split_lists:
            t_parser.words_list = question
            t_parser.lower_lists()
            assert t_parser.words_list == \
                    self.t_lowered_lists[counter]
            counter += 1

    def mock_words_list(self):
        words_list = []
        for word in self.tuple_list:
            words_list.append(word[1])
        return words_list

    def mock_word_list(self):
        word_list = []
        t_parser = Parser()
        for word in self.tuple_list:
            mock_word = self.MockWord()
            mock_word.index = word[0]
            mock_word.name = word[1]
            word_list.append(mock_word)
        return word_list

    def test_create_word(self):
        t_parser = Parser()
        t_parser.words_list = self.mock_words_list()
        t_parser.create_word()
        for word in t_parser.words_list:
            if word.index == 0:
                assert word.name == self.tuple_list[0][1]
            elif word.index == 3:
                assert word.name == self.tuple_list[3][1]
            elif word.index == 5:
                assert word.name == self.tuple_list[5][1]

    def test_enumerate_word(self):
        t_parser = Parser()
        t_parser.word_list = self.mock_word_list()
        t_parser.enumerate_word()

        for word in t_parser.word_list:
            if word.index == 0:
                assert word.enumeration == self.tuple_list[0][2]
            elif word.index == 3:
                assert word.enumeration == self.tuple_list[3][2]
            elif word.index == 5:
                assert word.enumeration == self.tuple_list[5][2]

    def mock_enumerate_word(self):
        word_list = []
        t_parser = Parser()
        for word in self.tuple_list:
            mock_word = self.MockWord()
            mock_word.index = word[0]
            mock_word.name = word[1]
            mock_word.enumeration = word[2]
            word_list.append(mock_word)
        return word_list

    def mock_next_word_enumeration(self):
        word_list = []
        t_parser = Parser()
        for word in self.tuple_list:
            mock_word = self.MockWord()
            mock_word.index = word[0]
            mock_word.name = word[1]
            mock_word.enumeration = word[2]
            mock_word.word_minus_one_enumeration = word[3]
            mock_word.word_plus_one_enumeration = word[4]
            mock_word.word_plus_two_enumeration = word[5]
            word_list.append(mock_word)
        return word_list


    def test_get_next_word_enumeration(self):

        t_parser = Parser()
        t_parser.word_list = self.mock_enumerate_word()
        t_parser.get_next_word_enumeration()
        for word in t_parser.word_list:
            if word.index == 0:
                assert word.word_minus_one_enumeration ==\
                        self.tuple_list[0][3]
                assert word.word_plus_one_enumeration ==\
                        self.tuple_list[0][4]
                assert word.word_plus_two_enumeration ==\
                        self.tuple_list[0][5]
            elif word.index == 3:
                assert word.word_minus_one_enumeration ==\
                        self.tuple_list[3][3]
                assert word.word_plus_one_enumeration ==\
                        self.tuple_list[3][4]
                assert word.word_plus_two_enumeration ==\
                        self.tuple_list[3][5]
            elif word.index == 5:
                assert word.word_minus_one_enumeration ==\
                        self.tuple_list[5][3]
                assert word.word_plus_one_enumeration ==\
                        self.tuple_list[5][4]
                assert word.word_plus_two_enumeration ==\
                        self.tuple_list[5][5]

    def test_find_start_word_position(self):
        t_parser = Parser()
        t_parser.word_list = self.mock_enumerate_word()
        t_parser.find_start_word_position()
        assert t_parser.start_word_index == self.tuple_list[4][0]

    def test_find_end_word_position(self):
        t_parser = Parser()
        t_parser.word_list = self.mock_next_word_enumeration()
        t_parser.start_word_index = self.tuple_list[4][0]
        t_parser.find_end_word_position()
        assert t_parser.end_word_index == self.tuple_list[5][0]

    def test_generate_parsed_string(self):
        t_parser = Parser()
        t_parser.word_list = self.mock_next_word_enumeration()
        t_parser.start_word_index = self.tuple_list[4][0]
        t_parser.end_word_index = self.tuple_list[5][0]
        t_parser.generate_parsed_string()
        assert t_parser.parsed_string == self.tuple_list[4][1]\
                +" "+self.tuple_list[5][1]
