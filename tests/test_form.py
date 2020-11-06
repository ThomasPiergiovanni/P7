"""
"""
from grandpy.form import Form

class TestForm:

    FORMULAR = Form()

    def test_ask_question(self):
        self.FORMULAR.ask_question()
        assert self.FORMULAR.question == "Ask your question here: \n"

