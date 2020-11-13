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
    survey.define_pattern()
    survey.get_prev_nexts_pattern()
    survey.get_start_position()
    survey.get_end_position()
    survey.get_search_element()

if __name__ == "__main__":
    main()
