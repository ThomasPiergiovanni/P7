"""Test parser module
"""
import pytest

from grandpy.parser.parser import Parser


@pytest.fixture(name="questions_list")
def fixture_questions_list():
    """Fixture function of question list.
    """
    questions = [
                "Où se trouve la Tour Eiffel?",
                "Quelle est l'adresse du Centre Commercial de Vélizy 2?",
                "Où est l'Arc de Triomphe?",
                "Dis-moi vieux con! C'est ou Saint-Laurent-des-Mortiers?",
                "Ey toi, tu sais c'est où Paris ou pas?",
                "Euuuh et sur Saint-Laurent-des-Mortiers"]
    return questions


@pytest.fixture(name="split_list")
def fixture_split_list():
    """Fixture function of questions split list.
    """
    questions_split = [
            ["Où", "se", "trouve", "la", "Tour", "Eiffel"],
            [
                    "Quelle", "est", "l", "adresse", "du", "Centre",
                    "Commercial", "de", "Vélizy", "2"],
            ["Où", "est", "l", "Arc", "de", "Triomphe"],
            [
                    "Dis-moi", "vieux", "con", "C", "est", "ou",
                    "Saint-Laurent-des-Mortiers"],
            [
                    "Ey", "toi", "tu", "sais", "c", "est", "où", "Paris",
                    "ou", "pas"],
            ["Euuuh", "et", "sur", "Saint-Laurent-des-Mortiers"]]
    return questions_split


@pytest.fixture(name="lowered_list")
def fixture_lowered_list():
    """Fixture function of lowered questions split list.
    """
    questions_split_lowered = [
            ["où", "se", "trouve", "la", "tour", "eiffel"],
            [
                    "quelle", "est", "l", "adresse", "du", "centre",
                    "commercial", "de", "vélizy", "2"],
            ["où", "est", "l", "arc", "de", "triomphe"],
            [
                    "dis-moi", "vieux", "con", "c", "est", "ou",
                    "saint-laurent-des-mortiers"],
            [
                    "ey", "toi", "tu", "sais", "c", "est", "où", "paris",
                    "ou", "pas"],
            ["euuuh", "et", "sur", "saint-laurent-des-mortiers"]]
    return questions_split_lowered


@pytest.fixture(name="parsed_chain")
def fixture_parsed_chain():
    """Fixture function of question parsed.
    """
    question_parsed = [
        ["tour eiffel"],
        ["centre commercial de vélizy 2"],
        ["arc de triomphe"],
        ["saint-laurent-des-mortiers"],
        ["paris"],
        ["saint-laurent-des-mortiers"]]
    return question_parsed


@pytest.fixture(name="question_one")
def fixture_question_one():
    """Fixture function of a question. It imitate a Word instances for
    a question
    """
    tuple_one = [
            (0, "où", None, None, "0", "0", "2", "0"),
            (1, "se", None, "0", "0", "2", "0", "1"),
            (2, "trouve", "0", "0", "2", "0", "1", "1"),
            (3, "la", "0", "2", "0", "1", "1", None),
            (4, "tour", "2", "0", "1", "1", None, None),
            (5, "eiffel", "0", "1", "1", None, None, None)]
    return tuple_one


@pytest.fixture(name="question_two")
def fixture_question_two():
    """Fixture function of a question. It imitate a Word instances for
    a question
    """
    tuple_two = [
            (0, "quelle", None, None, "0", "0", "0", "2"),
            (1, "est", None, "0", "0", "0", "2", "0"),
            (2, "l", "0", "0", "0", "2", "0", "1"),
            (3, "adresse", "0", "0", "2", "0", "1", "1"),
            (4, "du", "0", "2", "0", "1", "1", "0"),
            (5, "centre", "2", "0", "1", "1", "0", "1"),
            (6, "commercial", "0", "1", "1", "0", "1", "1"),
            (7, "de", "1", "1", "0", "1", "1", None),
            (8, "vélizy", "1", "0", "1", "1", None, None),
            (9, "2", "0", "1", "1", None, None, None)]
    return tuple_two


@pytest.fixture(name="question_three")
def fixture_question_three():
    """Fixture function of a question. It imitate a Word instances for
    a question
    """
    tuple_three = [
            (0, "ey", None, None, "1", "0", "0", "0"),
            (1, "toi", None, "1", "0", "0", "0", "0"),
            (2, "tu", "1", "0", "0", "0", "0", "0"),
            (3, "sais", "0", "0", "0", "0", "0", "0"),
            (4, "c", "0", "0", "0", "0", "0", "1"),
            (5, "est", "0", "0", "0", "0", "1", "0"),
            (6, "où", "0", "0", "0", "1", "0", "0"),
            (7, "paris", "0", "0", "1", "0", "0", None),
            (8, "ou", "0", "1", "0", "0", None, None),
            (9, "pas", "1", "0", "0", None, None, None)]
    return tuple_three


@pytest.fixture(name="question_four")
def fixture_question_four():
    """Fixture function of a question. It imitate a Word instances for
    a question
    """
    tuple_four = [
        (0, "euuuh", None, None, "0", "0", "0", "1"),
        (1, "et", None, "0", "0", "0", "1", None),
        (2, "sur", "0", "0", "0", "1", None, None),
        (3, "saint-laurent-des-mortiers", "0", "0", "1", None, None, None)]
    return tuple_four


class MockWord:
    """MockQuestion class
    """
    def __init__(self):
        self.index = None
        self.name = None
        self.min_two_enum = None
        self.min_one_enum = None
        self.enum = None
        self.plus_one_enum = None
        self.plus_two_enum = None
        self.plus_three_enum = None


def mock_words_list(question_tuple):
    """Function that mocks words list
    """
    words_list = []
    for element in question_tuple:
        words_list.append(element[1])
    return words_list


def mock_word_instances_list(question_tuple):
    """Function that mocks word instances list
    """
    word_instances_list = []
    for element in question_tuple:
        mock_word = MockWord()
        mock_word.index = element[0]
        mock_word.name = element[1]
        word_instances_list.append(mock_word)
    return word_instances_list


def mock_enumerate_word(question_tuple):
    """Function that mocks word enumeration
    """
    word_instances_list = []
    for element in question_tuple:
        mock_word = MockWord()
        mock_word.index = element[0]
        mock_word.name = element[1]
        mock_word.enum = element[4]
        word_instances_list.append(mock_word)
    return word_instances_list


def mock_enumerate_nexts_words(question_tuple):
    """Function that mocks next word enumeration
    """
    word_list = []
    for element in question_tuple:
        mock_word = MockWord()
        mock_word.index = element[0]
        mock_word.name = element[1]
        mock_word.min_two_enum = element[2]
        mock_word.min_one_enum = element[3]
        mock_word.enum = element[4]
        mock_word.plus_one_enum = element[5]
        mock_word.plus_two_enum = element[6]
        mock_word.plus_three_enum = element[7]
        word_list.append(mock_word)
    return word_list


def test_split_question_with_providing_questions(
        questions_list, split_list):
    """Function that test split question method with providing a list of
    questions for seeing if the split is done as expected
    """
    counter = 0
    for question in questions_list:
        parser = Parser()
        parser.question = question
        parser.split_question()
        assert parser.words_list == split_list[counter]
        counter += 1


def test_lower_lists_with_providing_list(split_list, lowered_list):
    """Function that test lower lists method with providing lists containing
    words for seeing if the words are lowered case as expected.
    """
    counter = 0
    for word_list in split_list:
        parser = Parser()
        parser.words_list = word_list
        parser.lower_lists()
        assert parser.words_list == lowered_list[counter]
        counter += 1


def test_create_word_with_providing_list_of_words_for_word_instanciation(
            question_one, question_two):
    """Function that test create word method with providing words list for
    seeing if the words are created as Word instances as expected.
    """
    def verifications(tuple_list):
        """Function that performs the comparison i.e. the verification if
        the tested method has done the job.
        """
        counter = 0
        for word in parser.words_list:
            if word.index == counter:
                assert word.name == tuple_list[counter][1]
            counter += 1

    # Test with one question
    parser = Parser()
    parser.words_list = mock_words_list(question_one)
    parser.create_word()
    verifications(question_one)

    # The same test but with another question
    parser = Parser()
    parser.words_list = mock_words_list(question_two)
    parser.create_word()
    verifications(question_two)


def test_enumerate_word_with_providing_word_instances(
            question_one, question_two):
    """Function that test enumerate word method with providing Word instances
    for seeing if the words are enumerated as expected.
    """
    def verifications(tuple_list):
        """Function that performs the comparison i.e. the verification if
        the tested method has done the job.
        """
        counter = 0
        for word in parser.word_instances_list:
            if word.index == counter:
                assert word.enum == tuple_list[counter][4]
            elif word.index == 3:
                assert word.enum == tuple_list[counter][4]
            elif word.index == 5:
                assert word.enum == tuple_list[counter][4]
            counter += 1

    # Test with one question
    parser = Parser()
    parser.word_instances_list = mock_word_instances_list(question_one)
    parser.enumerate_word()
    verifications(question_one)

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_word_instances_list(question_two)
    parser.enumerate_word()
    verifications(question_two)


def test_enumerate_nexts_words_with_providing_word_instances(
            question_one, question_two):
    """Function that test enumerate nexts words method with providing
    Word instances for seeing if the words nexts words are enumerated as
    expected.
    """
    def verifications(tuple_list):
        """Function that performs the comparison i.e. the verification if
        the tested method has done the job.
        """
        for word in parser.word_instances_list:
            if word.index == 0:
                assert word.min_two_enum == tuple_list[0][2]
                assert word.min_one_enum == tuple_list[0][3]
                assert word.plus_one_enum == tuple_list[0][5]
                assert word.plus_two_enum == tuple_list[0][6]
                assert word.plus_three_enum == tuple_list[0][7]
            elif word.index == 3:
                assert word.min_two_enum == tuple_list[3][2]
                assert word.min_one_enum == tuple_list[3][3]
                assert word.plus_one_enum == tuple_list[3][5]
                assert word.plus_two_enum == tuple_list[3][6]
                assert word.plus_three_enum == tuple_list[3][7]
            elif word.index == 5:
                assert word.min_two_enum == tuple_list[5][2]
                assert word.min_one_enum == tuple_list[5][3]
                assert word.plus_one_enum == tuple_list[5][5]
                assert word.plus_two_enum == tuple_list[5][6]
                assert word.plus_three_enum == tuple_list[5][7]

    # Test with one question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_word(question_one)
    parser.enumerate_nexts_words()
    verifications(question_one)

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_word(question_two)
    parser.enumerate_nexts_words()
    verifications(question_two)


def test_start_position_with_providing_word_instances(
            question_one, question_two, question_three, question_four):
    """Function that test start position method with providing
    Word instances for seeing if the the start position of the wanted parsed
    question is set to the expected  word.
    """

    # Test with one question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_word(question_one)
    parser.start_position()
    assert parser.start_index == question_one[4][0]

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_word(question_two)
    parser.start_position()
    assert parser.start_index == question_two[5][0]

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_word(question_three)
    parser.start_position()
    assert parser.start_index == question_three[7][0]

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_word(question_four)
    parser.start_position()
    assert parser.start_index == question_four[3][0]


def test_end_position_with_providing_word_instances(
        question_one, question_two, question_three, question_four):
    """Function that test end position method with providing
    Word instances for seeing if the the end position of the wanted parsed
    question is set to the expected  word.
    """

    # Test with one question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_nexts_words(question_one)
    parser.start_index = question_one[4][0]
    parser.end_position()
    assert parser.end_index == question_one[5][0]

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_nexts_words(question_two)
    parser.start_index = question_two[5][0]
    parser.end_position()
    assert parser.end_index == question_two[9][0]

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_nexts_words(question_three)
    parser.start_index = question_three[7][0]
    parser.end_position()
    assert parser.end_index == question_three[7][0]

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_nexts_words(question_four)
    parser.start_index = question_four[3][0]
    parser.end_position()
    assert parser.end_index == question_four[3][0]


def test_generate_parsed_chain_with_providing_word_instances(
            question_one, question_two, question_three,
            question_four, parsed_chain):
    """Function that test generate_parsed_chain method with providing
    Word instances for seeing if the parsed chain is set as expected.
    """

    # Test with one question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_nexts_words(question_one)
    parser.start_index = question_one[4][0]
    parser.end_index = question_one[5][0]
    parser.generate_parsed_chain()
    assert parser.parsed_chain == parsed_chain[0][0]

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_nexts_words(question_two)
    parser.start_index = question_two[5][0]
    parser.end_index = question_two[9][0]
    parser.generate_parsed_chain()
    assert parser.parsed_chain == parsed_chain[1][0]

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_nexts_words(question_three)
    parser.start_index = question_three[7][0]
    parser.end_index = question_three[7][0]
    parser.generate_parsed_chain()
    assert parser.parsed_chain == parsed_chain[4][0]
    print(parser.parsed_chain)

    # The same test but with another question
    parser = Parser()
    parser.word_instances_list = mock_enumerate_nexts_words(question_four)
    parser.start_index = question_four[3][0]
    parser.end_index = question_four[3][0]
    parser.generate_parsed_chain()
    assert parser.parsed_chain == parsed_chain[5][0]
