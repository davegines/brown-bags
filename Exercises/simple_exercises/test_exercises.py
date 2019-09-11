import unittest
from random import randint
from datetime import datetime
from Exercises.simple_exercises.exercises import SampleExercises as se


class SimpleTest(unittest.TestCase):
    def test_alphabet(self):
        self.assertEqual(se.alphabet_position("The sunset sets at twelve o' clock."),
                           "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(se.alphabet_position("The narwhal bacons at midnight."),
                           "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        self.assertEqual(se.alphabet_position(number_test), "")

    def test_count_smiley_faces(self):
        self.assertEqual(se.count_smileys([]), 0)
        self.assertEqual(se.count_smileys([':D', ':~)', ';~D', ':)']), 4)
        self.assertEqual(se.count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
        self.assertEqual(se.count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)

    def test_compare_array(self):
        self.assertEqual(se.order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        self.assertEqual(se.order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")

    def test_tribinocci(self):
        self.assertEqual(se.tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        self.assertEqual(se.tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
        self.assertEqual(se.tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
        self.assertEqual(se.tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
        self.assertEqual(se.tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(se.tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
        self.assertEqual(se.tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
        self.assertEqual(se.tribonacci([1, 1, 1], 1), [1])
        self.assertEqual(se.tribonacci([300, 200, 100], 0), [])
        self.assertEqual(se.tribonacci([0.5, 0.5, 0.5], 30),
                           [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5,
                            2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5,
                            900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])

    def test_tickets(self):
        self.assertEqual(se.tickets([25, 25, 50]), "YES")
        self.assertEqual(se.tickets([25, 100]), "NO")
        self.assertEqual(se.tickets([25, 25, 50, 50, 100]), "NO")
        self.assertEqual(se.tickets([25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]), "NO")

    def test_digital_root(self):
        self.assertEqual(se.digital_root(16), 7)
        self.assertEqual(se.digital_root(456), 6)

    def test_basic(self):
        self.assertEqual(se.is_prime(0),  False, "0  is not prime")
        self.assertEqual(se.is_prime(1),  False, "1  is not prime")
        self.assertEqual(se.is_prime(2),  True, "2  is prime")
        self.assertEqual(se.is_prime(73), True, "73 is prime")
        self.assertEqual(se.is_prime(75), False, "75 is not prime")
        self.assertEqual(se.is_prime(-1), False, "-1 is not prime")

    def test_remove_smallest(self):
        self.assertEqual(se.remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
        self.assertEqual(se.remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
        self.assertEqual(se.remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
        self.assertEqual(se.remove_smallest([]), [], "Wrong result for []")

    def test_sort_array(self):
        self.assertEqual(se.sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(se.sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        self.assertEqual(se.sort_array([]), [])

    def test_order(self):
        self.assertEqual(se.order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(se.order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
        self.assertEqual(se.order(""), "")

    def test_row_sum_odd_numbers(self):
        self.assertEqual(1, se.row_sum_odd_numbers(1))
        self.assertEqual(8, se.row_sum_odd_numbers(2))
        self.assertEqual(2197, se.row_sum_odd_numbers(13))
        self.assertEqual(6859, se.row_sum_odd_numbers(19))
        self.assertEqual(68921, se.row_sum_odd_numbers(41))

    def test_get_creditcard_number_empty_string(self):
        result = se.get_creditcard_number('')
        self.assertEqual('', result)

    def test_get_creditcard_number_all_characters(self):
        result = se.get_creditcard_number('1234')
        self.assertEqual('1234', result)

    def test_get_creditcard_number_split_characters(self):
        result = se.get_creditcard_number('0001234')
        self.assertEqual('###1234', result)

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


    # Integer to Roman numeral
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

    # Roman numeral to Integer
    def test_convert_roman_numeral_one(self):
        roman_numeral = se.convert_roman_numeral('I')
        self.assertEqual(1, roman_numeral)

    def test_convert_roman_numeral_three(self):
        roman_numeral = se.convert_roman_numeral('III')
        self.assertEqual(3, roman_numeral)

    def test_convert_roman_numeral_four(self):
        roman_numeral = se.convert_roman_numeral('IV')
        self.assertEqual(4, roman_numeral)

    def test_convert_roman_numeral_five(self):
        roman_numeral = se.convert_roman_numeral('V')
        self.assertEqual(5, roman_numeral)

    def test_convert_roman_numeral_six(self):
        roman_numeral = se.convert_roman_numeral('VI')
        self.assertEqual(6, roman_numeral)

    def test_convert_roman_numeral_nine(self):
        roman_numeral = se.convert_roman_numeral('IX')
        self.assertEqual(9, roman_numeral)

    def test_convert_roman_numeral_ten(self):
        roman_numeral = se.convert_roman_numeral('X')
        self.assertEqual(10, roman_numeral)




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
