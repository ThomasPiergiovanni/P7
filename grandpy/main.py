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
    # survey.find_keyword_in_pattern()
    survey.write_pattern()

    # survey.regular_expression_start()


if __name__ == "__main__":
    main()
