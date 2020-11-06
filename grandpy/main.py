"""
Main module
"""
from form import Form


def main():
    """
    Main method launching the programm
    """
    formular = Form()
    formular.ask_question()
    formular.see_question()

if __name__ == "__main__":
    main()
