"""
"""
from grandpy.parser.parser import Parser

class TestParser:

    class MockWord:
        def __init__(self):
            self.index = None
            self.name = None
            self.min_two_enum = None
            self.min_one_enum = None
            self.enum= None
            self.plus_one_enum = None
            self.plus_two_enum = None

    # t_question = "Où se trouve la Tour Eiffel?"
    t_questions_list = [
        "Où se trouve la Tour Eiffel?", 
        "Quelle est l'adresse du Centre Commercial de Vélizy 2?",
        "Où est l'Arc de Triomphe?",
        "Dis-moi vieux con! C'est ou Saint-Laurent-des-Mortiers?",
        "Ey toi, tu sais c'est où Paris ou pas?",
        "Euuuh et sur Saint-Laurent-des-Mortiers"
        ]
    t_split_lists = [
        ["Où","se","trouve","la","Tour","Eiffel"],
        ["Quelle","est","l","adresse","du","Centre","Commercial","de", "Vélizy", "2"],
        ["Où","est","l","Arc","de","Triomphe"],
        ["Dis-moi","vieux","con","C","est","ou","Saint-Laurent-des-Mortiers"],
        ["Ey","toi","tu","sais","c","est","où","Paris", "ou", "pas"],
        ["Euuuh", "et", "sur", "Saint-Laurent-des-Mortiers"]
        ]

    t_lowered_lists = [
        ["où","se","trouve","la","tour","eiffel"],
        ["quelle","est","l","adresse","du","centre","commercial","de", "vélizy", "2"],
        ["où","est","l","arc","de","triomphe"],
        ["dis-moi","vieux","con","c","est","ou","saint-laurent-des-mortiers"],
        ["ey","toi","tu","sais","c","est","où","paris", "ou", "pas"],
        ["euuuh", "et", "sur", "saint-laurent-des-mortiers"]
        ]
    t_parsed_string = [
        ["tour","eiffel"],
        ["centre","commercial","de", "vélizy", "2"],
        ["arc","de","triomphe"],
        ["saint-laurent-des-mortiers"],
        ["paris"],
        ["saint-laurent-des-mortiers"]
        ]


    tuple_one = [
            (0,"où", None, None,"0","0","2"),
            (1,"se",None,"0","0","2","0"),
            (2,"trouve","0","0","2","0","1"),
            (3,"la","0","2","0","1","1"),
            (4,"tour","2","0","1","1", None),
            (5,"eiffel","0","1","1", None, None)
            ]
    tuple_two = [
            (0,"quelle", None, None,"0","0","0"),
            (1,"est",None,"0","0","0","2"),
            (2,"l","0","0","0","2","0"),
            (3,"adresse","0","0","2","0","1"),
            (4,"du","0","2","0","1","1"),
            (5,"centre","2","0","1", "1", "0"),
            (6,"commercial","0","1","1","0","1"),
            (7,"de","1","1","0","1","1"),
            (8,"vélizy","1","0","1","1", None),
            (9,"2","0","1","1", None, None)
            ]

    tuple_three = [
            (0,"Ey", None, None,"1","0","0"),
            (1,"toi",None,"1","0","0","0"),
            (2,"tu","1","0","0","0","0"),
            (3,"sais","0","0","0","0","0"),
            (4,"c","0","0","0","0","0"),
            (5,"est","0","0","0", "0", "1"),
            (6,"où","0","0","0","1","0"),
            (7,"Paris","0","0","1","0","0"),
            (8,"ou","0","1","0","0", None),
            (9,"pas","1","0","0", None, None)
            ]
    tuple_four = [
            (0,"euuuh", None, None,"0","0","0"),
            (1,"et",None,"0","0","0","1"),
            (2,"sur","0","0","0","1",None),
            (3,"saint-laurent-des-mortiers","0","0","1", None, None)
            ]

    def mock_words_list(self, question_tuple):
        words_list = []
        for element in question_tuple:
            words_list.append(element[1])
        return words_list

    def mock_word_instances_list(self, question_tuple):
        word_instances_list = []
        t_parser = Parser()
        for element in question_tuple:
            mock_word = self.MockWord()
            mock_word.index = element[0]
            mock_word.name = element[1]
            word_instances_list.append(mock_word)
        return word_instances_list

    def mock_enumerate_word(self, question_tuple):
        word_instances_list = []
        t_parser = Parser()
        for element in question_tuple:
            mock_word = self.MockWord()
            mock_word.index = element[0]
            mock_word.name = element[1]
            mock_word.enum = element[4]
            word_instances_list.append(mock_word)
        return word_instances_list

    # def mock_next_word_enumeration(self):
    #     word_list = []
    #     t_parser = Parser(self.t_question)
    #     for word in self.tuple_list:
    #         mock_word = self.MockWord()
    #         mock_word.index = word[0]
    #         mock_word.name = word[1]
    #         mock_word.enumeration = word[2]
    #         mock_word.word_minus_one_enumeration = word[3]
    #         mock_word.word_plus_one_enumeration = word[4]
    #         mock_word.word_plus_two_enumeration = word[5]
    #         word_list.append(mock_word)
    #     return word_list

    def test_split_question_if_question_is_split_correctly(self):
        counter = 0 
        for question in self.t_questions_list:
            t_parser = Parser()
            t_parser.question = question
            t_parser.split_question()
            assert t_parser.words_list == self.t_split_lists[counter]
            counter += 1

    def test_lower_list_if_words_are_lowered_cases(self):
        counter = 0
        for word_list in self.t_split_lists:
            t_parser = Parser()
            t_parser.words_list = word_list
            t_parser.lower_lists()
            assert t_parser.words_list == \
                    self.t_lowered_lists[counter]
            counter += 1

    def test_create_word_ensure_word_instance_is_created_and_added_in_list(self):

        def verifications(tuple_list):
            counter = 0
            for word in t_parser.words_list:
                if word.index == counter:
                    assert word.name == tuple_list[counter][1]
                counter += 1

        # Test with one question            
        t_parser = Parser()
        t_parser.words_list =\
                self.mock_words_list(self.tuple_one)
        t_parser.create_word()
        verifications(self.tuple_one)

        # The same test but with another question  
        t_parser = Parser()
        t_parser.words_list =\
                self.mock_words_list(self.tuple_two)
        t_parser.create_word()
        verifications(self.tuple_two)

    def test_enumerate_word_verify_enumeration_is_correct(self):
        
        def verifications(tuple_list):
            counter = 0 
            for word in t_parser.word_instances_list:
                if word.index == counter:
                    assert word.enum == tuple_list[counter][4]
                elif word.index == 3:
                    assert word.enum== tuple_list[counter][4]
                elif word.index == 5:
                    assert word.enum == tuple_list[counter][4]
                counter += 1

        # Test with one question            
        t_parser = Parser()
        t_parser.word_instances_list =\
                self.mock_word_instances_list(self.tuple_one)
        t_parser.enumerate_word()
        verifications(self.tuple_one)

        # The same test but with another question  
        t_parser = Parser()
        t_parser.word_instances_list =\
                self.mock_word_instances_list(self.tuple_two)
        t_parser.enumerate_word()
        verifications(self.tuple_two)


    def test_enumerate_nexts_words_verify_next_enumeration_are_correct(self):

        def verifications(tuple_list):
            for word in t_parser.word_instances_list:
                if word.index == 0:
                    assert word.min_two_enum ==\
                            tuple_list[0][2]
                    assert word.min_one_enum ==\
                            tuple_list[0][3]
                    assert word.plus_one_enum ==\
                            tuple_list[0][5]
                    assert word.plus_two_enum ==\
                            tuple_list[0][6]
                elif word.index == 3:
                    assert word.min_two_enum ==\
                            tuple_list[3][2]
                    assert word.min_one_enum ==\
                            tuple_list[3][3]
                    assert word.plus_one_enum ==\
                            tuple_list[3][5]
                    assert word.plus_two_enum ==\
                            tuple_list[3][6]
                elif word.index == 5:
                    assert word.min_two_enum ==\
                            tuple_list[5][2]
                    assert word.min_one_enum ==\
                            tuple_list[5][3]
                    assert word.plus_one_enum ==\
                            tuple_list[5][5]
                    assert word.plus_two_enum ==\
                            tuple_list[5][6]

        # Test with one question            
        t_parser = Parser()
        t_parser.word_instances_list =\
                self.mock_enumerate_word(self.tuple_one)
        t_parser.enumerate_nexts_words()
        verifications(self.tuple_one)

        # The same test but with another question  
        t_parser = Parser()
        t_parser.word_instances_list =\
                self.mock_enumerate_word(self.tuple_two)
        t_parser.enumerate_nexts_words()
        verifications(self.tuple_two)

    def test_find_start_word_position(self):

        # Test with one question 
        t_parser = Parser()
        t_parser.word_instances_list = self.mock_enumerate_word(self.tuple_one)
        t_parser.find_start_word_position()
        assert t_parser.start_word_index == self.tuple_one[4][0]

        # The same test but with another question 
        t_parser = Parser()
        t_parser.word_instances_list = self.mock_enumerate_word(self.tuple_two)
        t_parser.find_start_word_position()
        assert t_parser.start_word_index == self.tuple_two[5][0]

        # The same test but with another question 
        t_parser = Parser()
        t_parser.word_instances_list = self.mock_enumerate_word(self.tuple_three)
        t_parser.find_start_word_position()
        assert t_parser.start_word_index == self.tuple_three[7][0]

        # The same test but with another question 
        t_parser = Parser()
        t_parser.word_instances_list = self.mock_enumerate_word(self.tuple_four)
        t_parser.find_start_word_position()
        assert t_parser.start_word_index == self.tuple_four[3][0]

    # def test_find_end_word_position(self):
    #     t_parser = Parser(self.t_question)
    #     t_parser.word_list = self.mock_next_word_enumeration()
    #     t_parser.start_word_index = self.tuple_list[4][0]
    #     t_parser.find_end_word_position()
    #     assert t_parser.end_word_index == self.tuple_list[5][0]

    # def test_generate_parsed_string(self):
    #     t_parser = Parser(self.t_question)
    #     t_parser.word_list = self.mock_next_word_enumeration()
    #     t_parser.start_word_index = self.tuple_list[4][0]
    #     t_parser.end_word_index = self.tuple_list[5][0]
    #     t_parser.generate_parsed_string()
    #     assert t_parser.parsed_string == self.tuple_list[4][1]\
    #             +" "+self.tuple_list[5][1]
