"""
Main module
"""
from grandpy.survey import Survey


def main():
    """
    Main method launching the programm
    """
    survey = Survey()
    # survey.split_question()
    # survey.normalize_lists()
    survey.define_word_code()
    survey.get_next_word_code()
    survey.find_start_word_position()
    survey.find_end_word_position()
    survey.generate_parsed_string()

if __name__ == "__main__":
    main()
