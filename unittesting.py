import unittest
import datetime_functions as DF


class UnitTesting(unittest.TestCase):
    """
    Unit testing for this project
    """

    def test_current_date(self):
        """
        Will test the function current_date
        :function location: ./datetime_functions.py
        """
        result = DF.current_date()
        self.assertEqual(str(type(result)), "<class 'str'>")
        self.assertEqual(len(result), 10)



if __name__ == '__main__':
    unittest.main()
