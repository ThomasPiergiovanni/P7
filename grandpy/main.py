"""
Main module
"""
from survey import Survey


def main():
    """
    Main method launching the programm
    """
    survey = Survey()
    survey.split_question()
    survey.normalize_lists()
    survey.filter_list()

if __name__ == "__main__":
    main()
