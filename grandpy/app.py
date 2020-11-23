"""
Main module
"""
from website import app
from grandpy.parser.parser import Parser
from grandpy.connection_manager import ConnectionManager


# def main():
#     """
#     Main method launching the programm
#     """
#     parser = Parser()
#     parser.ask_question()
#     parser.split_question()
#     parser.lower_lists()
#     parser.create_word()
#     parser.enumerate_word()
#     parser.get_next_word_enumeration()
#     parser.find_start_word_position()
#     parser.find_end_word_position()
#     parser.generate_parsed_string()

    # try_conn = ConnectionManager()
    # try_conn.get_places()

if __name__ == "__main__":
    # main()
    try_conn = ConnectionManager()
    # try_conn.get_places()
    try_conn.get_attribute()
