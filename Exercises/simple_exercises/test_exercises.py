import unittest
from Exercises.simple_exercises.exercises import SampleExercises as se


class SimpleTest(unittest.TestCase):
    # word wrap
    def test_word_wrap_should_return_the_word_if_column_wrap_number_is_greater_than_length_of_word(self):
        wrapped_content = se.word_wrap(word='a', wrap_at=100)
        self.assertEqual('a', wrapped_content)

    def test_word_wrap_should_return_the_word_if_column_wrap_number_is_equal_to_the_length_of_word(self):
        wrapped_content = se.word_wrap(word='abcd', wrap_at=4)
        self.assertEqual('abcd', wrapped_content)

    def test_word_wrap_should_return_one_line_wrap(self):
        wrapped_content = se.word_wrap(word='abcd', wrap_at=2)
        self.assertEqual('ab\rcd', wrapped_content)

    def test_word_wrap_should_wrap_on_partial_line(self):
        wrapped_content = se.word_wrap(word='abcde', wrap_at=2)
        self.assertEqual('ab\rcd\re', wrapped_content)

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
