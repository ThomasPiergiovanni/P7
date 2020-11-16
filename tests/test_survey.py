"""
"""
from grandpy.parser.parser import Parser

class TestParser:

    t_parser = Parser()
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
        ["Où","se","trouve","la","Tour","Eiffel"],
        ["Quelle","est","l","adresse","du","Centre","Commercial","de", "Vélizy", "2"],
        ["Où","se","trouve","l","Arc","de","Triomphe"],
        ["Dis-moi","vieux","con","C","est","ou","Saint-Laurent-des-Mortiers"],
        ["Ey","toi","tu","sais","c","est","où","chez", "moi"]
        ]

    t_filtered_list = [
        ["Tour","Eiffel"],
        ["Centre", "Centre", "de", "Vélizy", "2"],
        ["Arc","de", "Triomphe"],
        ["Saint-Laurent-des-Mortiers"],
        [""]
        ]

    def test_ask_question(self, monkeypatch):
        for question in self.t_questions_list:
            def mock_input(self):
                return question

            monkeypatch.setattr("builtins.input", mock_input)
            self.t_parser.ask_question()
            assert self.t_parser.question == question

    def test_split_question(self):
        counter = 0 
        for question in self.t_questions_list:
            self.t_parser.question = question 
            self.t_parser.split_question()
            assert self.t_parser.split_question_list == self.t_split_lists[counter]
            counter += 1

    def test_lower_question(self):
        pass

