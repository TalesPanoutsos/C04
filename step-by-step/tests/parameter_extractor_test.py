import sys
sys.path.append("../code")
import exemple_function_file as eff
import unittest
from parameter_extractor import *


class TestExtractInfo(unittest.TestCase):
    expected_results = [
        {
            "name": "mandatory_and_optional_params",
            "mandatory_params": [
                "some",
                "parameters"
            ],
            "optional_params": {
                "to": 1,
                "test": {}
            }
        },
        {
            "name": "only_mandatory_params",
            "mandatory_params": [
                "some",
                "parameters",
                "to",
                "test"
            ],
            "optional_params": {}
        },
        {
            "name": "only_optional_params",
            "mandatory_params": [],
            "optional_params": {
                "some": "some",
                "parameters": "parameters",
                "to": "to",
                "test": "test"
            }
        },
        {
            "name": "no_params",
            "mandatory_params": [],
            "optional_params": {}
        }
    ]

    def test_extract_info(self):
        self.assertEqual(extract_info(eff.mandatory_and_optional_params),
                         self.expected_results[0])
        self.assertEqual(extract_info(eff.only_mandatory_params),
                         self.expected_results[1])
        self.assertEqual(extract_info(eff.only_optional_params),
                         self.expected_results[2])
        self.assertEqual(extract_info(eff.no_params),
                         self.expected_results[3])

    # Testing this function, the get_module_functions is also implicitly tested
    def test_get_module_functions_info(self):
        result = get_module_functions_info('exemple_function_file.py')

        # Because they may be out of order
        self.assertEqual(
            [i in result for i in self.expected_results], [1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
