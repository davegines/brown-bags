from CodeReadability.finder import *
from unittest import TestCase


class UnitTests(TestCase):
    def test_null_input_should_return_none(self):
        finder = Finder()
        result = finder.find(None)
        self.assertIsNone(result)

    def test_one_input_should_return_that_one(self):
        finder = Finder()
        p = P('Saul', 1)
        result = finder.find([p])
        self.assertEqual(p, result)

    def test_multiple_of_same_age_should_last_person_in_list(self):
        finder = Finder()
        p1 = P('Saul', 1)
        p2 = P('Harry', 1)
        result = finder.find([p1, p2])
        self.assertEqual(p2, result)
