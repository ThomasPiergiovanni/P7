"""
"""
from grandpy.survey import Survey

class TestSurvey:

    survey = Survey()
    questions_list = [
        "Où se trouve la Tour Eiffel", 
        "Quelle est l'adresse du Centre Commercial de Vélizy 2",
        "Où se trouve l'Arc de Triomphe",
        "Dis-moi vieux con, c'est ou Saint-Laurent-des-Mortiers"
        ]
    split_lists = [
        ["Où","se","trouve","la","Tour","Eiffel"],
        ["Quelle","est","l","adresse","du","Centre","Commercial","de", "Vélizy", "2"],
        ["Où","se","trouve","l","Arc","de","Triomphe"],
        ["Dis-moi","vieux","con","c","est","ou","Saint-Laurent-des-Mortiers"]
        ]
    filtered_list = [
        ["Tour","Eiffel"],
        ["Centre","Centre", "de", "Vélizy", "2"]
        ["Arc","de", "Triomphe"]
        ["Saint-Laurent-des-Mortiers"]
    ]

    def test_ask_question(self, monkeypatch):
        for question in self.questions_list:
            def mock_input(self):
                return question

            # monkeypatch.setattr("builtins.input", mock_input)
            # result = input("Quelle est votre question?")
            # assert result == question

            monkeypatch.setattr("builtins.input", mock_input)
            self.survey.ask_question()
            assert self.survey.question == question

    def test_split_question(self):
        counter = 0 
        for question in self.questions_list:
            self.survey.question = question 
            self.survey.split_question()
            assert self.survey.split_list == self.split_lists[counter]
            counter += 1


