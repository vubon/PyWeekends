import json
import unittest

from PyWeekends.output_formatter import OutputFormatter


class TestOutputFormatter(unittest.TestCase):

    def test_as_json(self):
        data = {'January': ['5', '6', '12', '13', '19', '20', '26', '27']}
        formatter = OutputFormatter(data)
        expected_json = json.dumps(data)
        self.assertEqual(formatter.as_json(), expected_json)

    def test_as_json_invalid(self):
        # Test with non-dictionary or non-list data
        formatter = OutputFormatter('invalid_data')
        with self.assertRaises(TypeError):
            formatter.as_json()

        # Test with invalid JSON data
        formatter = OutputFormatter({"January", "February"})
        with self.assertRaises(TypeError):
            formatter.as_json()
