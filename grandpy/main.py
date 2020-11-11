"""
Main module
"""
from survey import Survey


def main():
    """
    Main method launching the programm
    """
    survey = Survey()
    # survey.split_question()
    # survey.normalize_lists()
    # survey.filter_list()
    # survey.write_pattern()
    survey.regular_expression_start()
    #survey.regular_expression_end()

if __name__ == "__main__":
    main()
