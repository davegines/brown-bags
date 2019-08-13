class SampleExercises:
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
