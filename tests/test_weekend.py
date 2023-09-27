import unittest
import json
from PyWeekends import Weekend, WeekendStart


class TestWeekend(unittest.TestCase):

    def test_all_weekends(self):
        w = Weekend(year=2024)
        weekends = w.all_weekends(enable_month_name=True).as_json()
        expected_weekends = {
            'January': ['6', '7', '13', '14', '20', '21', '27', '28'],
            'February': ['3', '4', '10', '11', '17', '18', '24', '25'],
            'March': ['2', '3', '9', '10', '16', '17', '23', '24', '30', '31'],
            'April': ['6', '7', '13', '14', '20', '21', '27', '28'],
            'May': ['4', '5', '11', '12', '18', '19', '25', '26'],
            'June': ['1', '2', '8', '9', '15', '16', '22', '23', '29', '30'],
            'July': ['6', '7', '13', '14', '20', '21', '27', '28'],
            'August': ['3', '4', '10', '11', '17', '18', '24', '25', '31'],
            'September': ['1', '7', '8', '14', '15', '21', '22', '28', '29'],
            'October': ['5', '6', '12', '13', '19', '20', '26', '27'],
            'November': ['2', '3', '9', '10', '16', '17', '23', '24', '30'],
            'December': ['1', '7', '8', '14', '15', '21', '22', '28', '29']
        }

        self.assertEqual(json.loads(weekends), expected_weekends)

    def test_month_weekends(self):
        w = Weekend(year=2024, weekend_start=WeekendStart.FRIDAY)
        january_weekends = w.month_weekends('January').as_json()
        expected_january_weekends = ['5', '6', '12', '13', '19', '20', '26', '27']
        self.assertEqual(json.loads(january_weekends), expected_january_weekends)

    def test_month_weekends_invalid_month(self):
        w = Weekend(year=2024, weekend_start=WeekendStart.FRIDAY)
        with self.assertRaises(ValueError):
            w.month_weekends('InvalidMonth')

    def test_month_weekends_invalid_month_case(self):
        w = Weekend(year=2024, weekend_start=WeekendStart.FRIDAY)
        with self.assertRaises(ValueError):
            w.month_weekends('jaNuARy4')  # Invalid case

    def test_month_weekends_invalid_year(self):
        # Test with a year in the future
        w = Weekend(year=454545, weekend_start=WeekendStart.FRIDAY)
        with self.assertRaises(ValueError):
            w.month_weekends('January')
