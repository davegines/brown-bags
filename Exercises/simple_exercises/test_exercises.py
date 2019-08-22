import unittest
from datetime import datetime
from Exercises.simple_exercises.exercises import SampleExercises as se


class SimpleTest(unittest.TestCase):
    # Remove duplicate words
    def test_remove_duplicate_words_none_exist(self):
        phrase = 'alpha'
        result = se.remove_duplicate_words(phrase)
        self.assertEqual('alpha', result)

    def test_remove_duplicate_words_one_duplicate(self):
        phrase = 'alpha beta alpha'
        result = se.remove_duplicate_words(phrase)
        self.assertEqual('alpha beta', result)

    def test_remove_duplicate_words_multiple_duplicates(self):
        phrase = 'alpha beta alpha alpha beta delta alpha'
        result = se.remove_duplicate_words(phrase)
        self.assertEqual('alpha beta delta', result)


    # Dictionary replacer
    def test_dict_replacer_no_phrase(self):
        phrase = ''
        dictionary = {}
        result = se.dict_replacer(phrase, dictionary)
        self.assertEqual('', result)

    def test_dict_replacer_one_item_phrase(self):
        phrase = '<a>'
        dictionary = {
            'a': 'successful'
        }
        result = se.dict_replacer(phrase, dictionary)
        self.assertEqual('successful', result)

    def test_dict_replacer_two_items_phrase(self):
        phrase = 'I think <1> lives in <2>.'
        dictionary = {
            '1': 'Nate',
            '2': 'Idaho'
        }
        result = se.dict_replacer(phrase, dictionary)
        self.assertEqual('I think Nate lives in Idaho.', result)


    # Roman numeral
    def test_get_roman_numeral_one(self):
        roman_numeral = se.get_roman_numeral(1)
        self.assertEqual('I', roman_numeral)

    def test_get_roman_numeral_three(self):
        roman_numeral = se.get_roman_numeral(3)
        self.assertEqual('III', roman_numeral)

    def test_get_roman_numeral_four(self):
        roman_numeral = se.get_roman_numeral(4)
        self.assertEqual('IV', roman_numeral)

    def test_get_roman_numeral_five(self):
        roman_numeral = se.get_roman_numeral(5)
        self.assertEqual('V', roman_numeral)

    def test_get_roman_numeral_six(self):
        roman_numeral = se.get_roman_numeral(6)
        self.assertEqual('VI', roman_numeral)

    def test_get_roman_numeral_nine(self):
        roman_numeral = se.get_roman_numeral(9)
        self.assertEqual('IX', roman_numeral)

    def test_get_roman_numeral_ten(self):
        roman_numeral = se.get_roman_numeral(10)
        self.assertEqual('X', roman_numeral)




    def test_palindrome(self):
        test_function = se.is_palindrome()
        self.assertTrue(test_function('Doc, note: I dissent. A fast never prevents a fatness. I diet on cod'))
        self.assertFalse(test_function('I am not one for sure'))
        self.assertTrue(test_function('Able was I ere I saw Elba'))
        self.assertTrue(test_function('Never odd or even'))
        self.assertTrue(test_function('aabbccddeefeeddccbbaa'))
        self.assertFalse(test_function('abbccddeeffeddccbbaa'))

    def test_string_parse(self):
        developer_likes_and_dislikes = """

        +------------------------------------+-----------------------------------+
        | likes                              | dislikes                          |
        +------------------------------------+-----------------------------------+
        | Meritocracy                        | Favoritism, ass-kissing, politics |
        +------------------------------------+-----------------------------------+
        | Healthy debates and collaboration  | Ego-driven rhetoric, drama and FUD|
        |                                    | to get one's way                  |
        +------------------------------------+-----------------------------------+
        | Autonomy given by confident leaders| Micro-management by insecure      |
        | capable of attracting top-tier     | managers compensating for a weak, |
        | talent                             | immature team                     |
        +------------------------------------+-----------------------------------+
        | Fluid communication, brief, ad-hoc | Formal meetings, endless debate   |
        | discussions, white-boarding, and   |                                   |
        | quick but informed decisions       |                                   |
        +------------------------------------+-----------------------------------+
        | Where else can I help out?         | I'm blocked by..., I only know how|
        |                                    | to...                             |
        +------------------------------------+-----------------------------------+
        | Getting things done.               | Contrived company culture         |
        +------------------------------------+-----------------------------------+
        | Clever and disruptive business     |                                   |
        | ideas that solve real and immediate|                                   |
        | needs in a marketplace             |                                   |
        +------------------------------------+-----------------------------------+
        | Software and system abstractions   | Hard-coding, brute-force          |
        +------------------------------------+-----------------------------------+
        | Frameworks and best-practices      | Hermetic code-base                |
        +------------------------------------+-----------------------------------+
        | Best tool for the job              | One size fits all                 |
        +------------------------------------+-----------------------------------+
        | Simple design                      | Over-engineering                  |
        +------------------------------------+-----------------------------------+
        | Leveraging open-source             | Re-inventing the wheel            |
        +------------------------------------+-----------------------------------+
        | Practical solutions to business    | Let's do this or use that because |
        | core competency                    | it's new and cool                 |
        +------------------------------------+-----------------------------------+
        | Building solutions to current      | Over-emphasizing "nice-to-haves"  |
        | business needs and customer demand | and conjecture                    |
        +------------------------------------+-----------------------------------+

        """
        answer = se.string_parse(developer_likes_and_dislikes)
        self.assertEqual(answer, [
            (u'Meritocracy', u'Favoritism, ass-kissing, politics'),
            (u'Healthy debates and collaboration',
             u"Ego-driven rhetoric, drama and FUD to get one's way"),
            (u'Autonomy given by confident leaders capable of attracting top-tier talent',
             u'Micro-management by insecure managers compensating for a weak, immature team'),
            (u'Fluid communication, brief, ad-hoc discussions, white-boarding, and quick but informed decisions',
             u'Formal meetings, endless debate'),
            (u'Where else can I help out?', u"I'm blocked by..., I only know how to..."),
            (u'Getting things done.', u'Contrived company culture'),
            (u'Clever and disruptive business ideas that solve real and immediate needs in a marketplace',
             u''),
            (u'Software and system abstractions', u'Hard-coding, brute-force'),
            (u'Frameworks and best-practices', u'Hermetic code-base'),
            (u'Best tool for the job', u'One size fits all'),
            (u'Simple design', u'Over-engineering'),
            (u'Leveraging open-source', u'Re-inventing the wheel'),
            (u'Practical solutions to business core competency',
             u"Let's do this or use that because it's new and cool"),
            (u'Building solutions to current business needs and customer demand',
             u'Over-emphasizing "nice-to-haves" and conjecture')
        ])

    # word wrap
    def test_word_wrap_should_return_the_word_if_column_wrap_number_is_greater_than_length_of_word(self):
        wrapped_content = se.word_wrap(word='a', wrap_at=100)
        self.assertEqual('a', wrapped_content)

    def test_word_wrap_should_return_the_word_if_column_wrap_number_is_equal_to_the_length_of_word(self):
        wrapped_content = se.word_wrap(word='abcd', wrap_at=4)
        self.assertEqual('abcd', wrapped_content)

    def test_word_wrap_should_return_one_line_wrap(self):
        wrapped_content = se.word_wrap(word='abcd', wrap_at=2)
        self.assertEqual('ab\ncd', wrapped_content)

    def test_word_wrap_should_wrap_on_partial_line(self):
        wrapped_content = se.word_wrap(word='abcde', wrap_at=2)
        self.assertEqual('ab\ncd\ne', wrapped_content)

    # word wrap2
    def test_word_wrap2_should_return_the_word_if_column_wrap_number_is_greater_than_length_of_word(self):
        wrapped_content = se.word_wrap2(word='a', wrap_at=100)
        self.assertEqual('a', wrapped_content)

    def test_word_wrap2_should_return_the_word_if_column_wrap_number_is_equal_to_the_length_of_word(self):
        wrapped_content = se.word_wrap2(word='abcd', wrap_at=4)
        self.assertEqual('abcd', wrapped_content)

    def test_word_wrap2_should_return_one_line_wrap(self):
        wrapped_content = se.word_wrap2(word='abcd', wrap_at=2)
        self.assertEqual('ab\ncd', wrapped_content)

    def test_word_wrap2_should_wrap_on_partial_line(self):
        wrapped_content = se.word_wrap2(word='abcde', wrap_at=2)
        self.assertEqual('ab\ncd\ne', wrapped_content)

    # get_adjacent_elements_with_max_product
    def test_empty_array_should_return_none(self):
        result = se.get_adjacent_elements_with_max_product([])
        self.assertIsNone(result)

    def test_array_with_item_of_1_should_return_1(self):
        result = se.get_adjacent_elements_with_max_product([1])
        self.assertEqual(1, result)

    def test_array_with_2_3_should_return_6(self):
        result = se.get_adjacent_elements_with_max_product([2, 3])
        self.assertEqual(6, result)

    def test_array_with_item_of_10_should_return_10(self):
        result = se.get_adjacent_elements_with_max_product([10])
        self.assertEqual(10, result)

    def test_array_with_4_5_should_return_20(self):
        result = se.get_adjacent_elements_with_max_product([4, 5])
        self.assertEqual(20, result)

    def test_array_with_2_3_4_should_return_12(self):
        result = se.get_adjacent_elements_with_max_product([2, 3, 4])
        self.assertEqual(12, result)

    def test_array_with_0_neg5_6_should_return_0(self):
        result = se.get_adjacent_elements_with_max_product([0, -5, 6])
        self.assertEqual(0, result)


    # are_anagrams
    def test_are_anagramss(self):
        are_anagrams = se.are_anagrams('listen', 'silent')
        self.assertTrue(are_anagrams)
