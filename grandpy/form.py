"""
form module
"""

class Form:
    """
    """
    def __init__(self):
        self.question_label = "Ask your question here: \n"
        self.question = None
        self.address_answer = None
        self.random_info_answer = None

    def ask_question(self):
        """
        """
        #self.question = input(self.question_label)
        self.question = self.question_label


    def see_question(self):
        """
        """
        print("Question asked by user: ",self.question)



