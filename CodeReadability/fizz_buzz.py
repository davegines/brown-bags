class FizzBuzz:
    def execute(self, numbers):
        results = []

        for n in numbers:
            if n % 3 == 0 or n % 5 == 0:
                if n % 3 == 0 and n % 5 == 0:
                    results.append('fizz buzz')
                elif n % 3 == 0:
                    results.append('fizz')
                elif n % 5 == 0:
                    results.append('buzz')
            else:
                results.append(n)

        return results
