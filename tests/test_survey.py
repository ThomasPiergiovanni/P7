"""
"""
from grandpy.survey import Survey

class TestSurvey:

    survey = Survey()
    questions_list = [
        "Où se trouve la Tour Eiffel", 
        "Quelle est l'adresse du Centre Commercial de Vélizy 2",
        "Comment vas ta mère",
        "",
        1234,
        é&1/
        ]

    def test_ask_question(self, monkeypatch):
        for question in self.questions_list:
            def mock_input(self):
                return answer

            monkeypatch.setattr("builtins.input", mock_input)
            result = input("Quelle est votre question?")
            assert result == question

    def test_parser(self):
        pass
        # question = "Quelle est l'adresse de l'Elysée"

        # def mock_parser

        # self.survey.parse_question()
        # assert self.survey.address_answer == "c est ici"
