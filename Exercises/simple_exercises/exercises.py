from datetime import datetime, timedelta
import re


class SampleExercises:
    # Dept meeting Aug 22, 2019
    @staticmethod
    def get_roman_numeral(int_number):
        return ''

    # Dept meeting Aug 22, 2019
    @staticmethod
    def remove_duplicate_words(phrase):
        return ''

    # Dept meeting Aug 22, 2019
    @staticmethod
    def dict_replacer(phrase, dictionary):
        return ''




    @staticmethod
    def dynamic_classes(names):
        new_classes = []

        @classmethod
        def is_the_one(cls):
            return cls.__name__.lower() == 'neo'

        for n in names:
            new_classes.append(type(n, (object,), {'is_the_one': is_the_one}))

        return new_classes

        """get_dynamic_classes: Needs to return a list of classes that are dynamically created that each have a 
        function named is_the_one that will return true if the class name is Neo otherwise false.
        """

    @staticmethod
    def likes_and_dislikes(text):
        developer_likes_and_dislikes = """+------------------------------------+-----------------------------------+
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
| Clever and disruptive business     |                                   |
| ideas that solve real and immediate|                                   |
| needs in a marketplace             |                                   |
+------------------------------------+-----------------------------------+
"""
        likes_and_dislikes = []
        records = developer_likes_and_dislikes.split('+------------------------------------+-----------------------------------+')

        for record in records[2:]:
            lines = record.split('\n')
            like = ''
            dislike = ''

            for line in lines[1:-1]:
                like += line[2: 37].rstrip() + ' '
                dislike += line[39: -1].rstrip() + ' '
            likes_and_dislikes.append((like.rstrip(), dislike.rstrip()))

    @staticmethod
    def month_last_day(dt):
        if dt.month == 12:
            return 31
        last_day = dt.replace(month=dt.month + 1, day=1) - timedelta(days=1)
        return last_day.day
        """
        month_last_day: Needs to return the last day of the month as an integer
        :return:
        """

    @staticmethod
    def week_start_end(dt):
        today = dt
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        return (datetime.combine(start, datetime.min.time()), datetime.combine(end, datetime.max.time()))

    @staticmethod
    def dict_key_values_swapped(d):
        resp = {}
        for i in dict.items(d):
            resp[i[1]] = i[0]
        return resp
        """
        reverse_dict: Needs to return the dictionary provided by with the values as the keys and the keys as the values
        """

    @staticmethod
    def string_parse(text):
        likes_and_dislikes = []
        records = text.split('+------------------------------------+-----------------------------------+')

        for record in records[2:]:
            if record.find('|') < 0:
                continue
            start_idx = record.find('|') + 1
            start_break_idx = record.index('|', start_idx) - 1
            end_idx = record.index('|', start_break_idx + 2) - 1
            end_break_idx = start_break_idx + 2
            lines = record.split('\n')[1: -1]
            like = ''
            dislike = ''

            for line in lines:
                like += line[start_idx: start_break_idx].rstrip() + ' '
                dislike += line[end_break_idx: end_idx].rstrip() + ' '
            likes_and_dislikes.append((like.rstrip(), dislike.rstrip()))

        return likes_and_dislikes

    @staticmethod
    def sorted_dict_desc(fruit_dict):
        return sorted(fruit_dict, key=lambda f: f['count'])

    @staticmethod
    def greater_than_avg(nums):
        avg = sum(nums) / len(nums)
        greater_than_avg = [n for n in nums if n > avg]
        return greater_than_avg

        """
        :param nums:
        :return:
        self.assertEqual([3], self.solutions.greater_than_avg([1, 2, 3]))
        self.assertEqual([8, 5, 11], self.solutions.greater_than_avg([-1, 8, 0, 4, 5, 2, 11]))
        """

    @staticmethod
    def is_palindrome():
        def test_function(word):
            re_alpha_only = '[^A-Za-z0-9]+'
            w1 = re.sub(re_alpha_only, '', word.lower())
            w2 = re.sub(re_alpha_only, '', word[::-1].lower())

            return w1 == w2
        return test_function

    @staticmethod
    def word_wrap(word, wrap_at):
        length_of_word = len(word)
        if length_of_word > wrap_at:
            first_part_of_word = word[:wrap_at] + '\n'
            remainder_of_word = word[wrap_at:]
            return first_part_of_word + SampleExercises.word_wrap(remainder_of_word, wrap_at)
        return word

    @staticmethod
    def word_wrap2(word, wrap_at):
        length_of_word = len(word)
        if length_of_word > wrap_at:
            formatted_word = ''
            while length_of_word > wrap_at:
                first_part_of_word = word[:wrap_at] + '\n'
                formatted_word += first_part_of_word
                word = word[wrap_at:]
                length_of_word = len(word)
            if length_of_word > 0:
                formatted_word += word
            return formatted_word.rstrip('\n')
        else:
            return word

    @staticmethod
    def get_adjacent_elements_with_max_product(int_array):
        if len(int_array) == 1:
            return int_array[0]
        elif len(int_array) > 1:
            max_val = int_array[0] * int_array[1]
            for x in (range(1, len(int_array) - 1)):
                new_val = int_array[x] * int_array[x + 1]
                if new_val > max_val:
                    max_val = new_val
            return max_val

        return None

    '''Given two strings, return whether or not they are anagrams'''
    @staticmethod
    def are_anagrams(s1, s2):
        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] = c1[pos] + 1

        for i in range(len(s2)):
            pos = ord(s2[i]) - ord('a')
            c2[pos] = c2[pos] + 1

        j = 0
        still_ok = True
        while j < 26 and still_ok:
            if c1[j] == c2[j]:
                j = j + 1
            else:
                still_ok = False

        return still_ok
