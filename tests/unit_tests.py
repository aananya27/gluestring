import unittest
from gluestring.glue_def import glue_it

# configs:
dictionary_test_1 = {
    "first_item": "ABC",
    "second_item": "DEF",
    "third_item": "VALUE_3",
    "default": "NA"
}
dictionary_test_2 = {
    "A item": "abcABC",
    "B item": "defDEF",
    "C item": "ghiGHI",
    "default": "hmmm"
}
test_string_1 = 'some text before {{first_item}} & {{second_item}}'
test_string_2 = '{{A item}} && {{ hi }} && {{C item}}'


class TestUtils(unittest.TestCase):
    def test_glue_it(self):

        test_result1 = glue_it(test_string_1, dictionary_test_1)
        test_result2 = glue_it(test_string_2, dictionary_test_2)
        self.assertEqual(test_result1, 'some text before ABC & DEF')
        self.assertEqual(
            test_result2, 'some text before abcABC && hmmm && ghiGHI')


if __name__ == '__main__':
    unittest.main()


# python -m unittest tests.unit_tests
