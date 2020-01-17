class Dni:
    LETTERS = 'TRWAGMYFPDXBNJZSQVHLCKE'
    def validate(self, dni_number):
        self._check_digits(dni_number)
        position = int(dni_number) % 23
        return self.LETTERS[position]

    def _check_digits(self, dni_number):
        self._check_positive_numbers(dni_number)
        self._check_length(dni_number)

    def _check_length(self, dni_number):
        if len(dni_number) != 8:
            raise DniMustHaveEightDigits

    def _check_positive_numbers(self, dni_number):
        try:
            if int(dni_number) < 0:
                raise DniMustBeenPositiveNumbers
        except ValueError:
            raise DniMustBeenPositiveNumbers
        

class DniMustHaveEightDigits(Exception):
    pass

class DniMustBeenPositiveNumbers(Exception):
    pass