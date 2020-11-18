"""
Main module
"""
from grandpy.parser.parser import Parser


def main():
    """
    Main method launching the programm
    """
    parser = Parser()
    parser.ask_question()
    parser.split_question()
    parser.lower_lists()
    parser.create_word()
    parser.enumerate_word()
    parser.get_next_word_enumeration()
    # parser.find_start_word_position()
    # parser.find_end_word_position()
    # parser.generate_parsed_string()

if __name__ == "__main__":
    main()
