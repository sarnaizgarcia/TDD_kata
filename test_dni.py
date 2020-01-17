LETTERS = 'TRWAGMYFPDXBNJZSQVHLCKE'

import unittest
import pytest

from dni import Dni, DniMustHaveEightDigits, DniMustBeenPositiveNumbers

class TestDni(unittest.TestCase):
    def setUp(self):
        self.dni = Dni()

    def test_error_when_dni_has_no_eigth_digits(self):
        dni_number = '2252517'

        with pytest.raises(DniMustHaveEightDigits):
            self.dni.validate(dni_number)

    def test_number_it_has_no_negative_numbers(self):
        dni_number = '-1523587'

        with pytest.raises(DniMustBeenPositiveNumbers):
            self.dni.validate(dni_number)

    def test_dni_digits_are_all_numbers(self):
        dni_number = 'not a number'

        with pytest.raises(DniMustBeenPositiveNumbers):
            self.dni.validate(dni_number)

    def test_first_concurrence(self):
        dni_number = '00000023'

        letter = self.dni.validate(dni_number)

        assert letter == 'T'
    
    def test_second_concurrence(self):
        dni_number = '00000024'

        letter = self.dni.validate(dni_number)

        assert letter == 'R'

        