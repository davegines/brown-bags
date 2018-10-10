class SampleExercises:
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
