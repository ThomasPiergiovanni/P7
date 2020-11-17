"""
"""
from grandpy.parser.parser import Parser

class TestParser:

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

    t_filtered_list = [
        ["Tour","Eiffel"],
        ["Centre", "Centre", "de", "Vélizy", "2"],
        ["Arc","de", "Triomphe"],
        ["Saint-Laurent-des-Mortiers"],
        [""]
        ]

    def test_ask_question(self, monkeypatch):
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
            assert t_parser.split_question_list == self.t_split_lists[counter]
            counter += 1

    def test_lower_list_for_split_question_list(self):
        t_parser = Parser()
        counter = 0
        for question in self.t_split_lists:
            t_parser.split_question_list = question
            t_parser.lower_lists()
            assert t_parser.split_question_list == \
                    self.t_lowered_lists[counter]
            counter += 1

    def test_enumerate_word(self):

        t_parser = Parser()
        t_enumerate_words_tuple = [("où","0"), ("se","0"),
            ("trouve","2"), ("la","0"), ("tour","1"), ("eiffel","1")]
        t_word_mock_list = []

        class MockWord:
            def __init__(self):
                self.name = None
                self.index = None
                self.enumeration = None

        counter = 0
        for word in t_enumerate_words_tuple:
            mock_word = MockWord()
            mock_word.index = counter
            mock_word.name = word[0]
            mock_word.enumeration = word[1]
            t_word_mock_list.append(mock_word)
            t_parser.split_question_list.append(word[0])
            counter += 1
        t_parser.enumerate_word()
        for word in t_parser.words_list:
            word_mock_enumeration = [mock_word.enumeration for mock_word
                    in t_word_mock_list if mock_word.index == word.index]
            assert word.enumeration == word_mock_enumeration[0]

    def test_get_next_word_enumeration(self):

        # Tuple structure: (index, word, enumeration, enumeration tuple-1
        # enumeration tuple+1, enumeration tuple+2)
        t_enumerate_words_tuple = [
                (0,"où","0",None,"0","2"),
                (1,"se","0","0","2","0"),
                (2,"trouve","2","0","0","1"),
                (3,"la","0","2","1","1"),
                (4,"tour","1","0","1",None),
                (5,"eiffel","1","1", None ,None)]
        class MockWord:
            def __init__(self):
                self.index = None
                self.name = None
                self.enumeration = None
                self.word_minus_one_enumeration = None
                self.word_plus_one_enumeration = None
                self.word_plus_two_enumeration = None

        t_parser = Parser()
        for word in t_enumerate_words_tuple:
            mock_word = MockWord()
            mock_word.index = word[0]
            mock_word.name = word[1]
            mock_word.enumeration = word[2]
            t_parser.words_list.append(mock_word)
        t_parser.get_next_word_enumeration()
        for word in t_parser.words_list:
            if word.index == 0:
                assert word.word_minus_one_enumeration == None
                assert word.word_plus_one_enumeration == "0"
                assert word.word_plus_two_enumeration == "2"
            elif word.index == 3:
                assert word.word_minus_one_enumeration == "2"
                assert word.word_plus_one_enumeration == "1"
                assert word.word_plus_two_enumeration == "1"
            elif word.index == 5:
                assert word.word_minus_one_enumeration == "1"
                assert word.word_plus_one_enumeration == None
                assert word.word_plus_two_enumeration == None




        


