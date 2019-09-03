import unittest
from gluestring.main import glue_it

# configs:
dictionary_test_1 = {
    "item1": "ABC",
    "item2": "DEF",
    "item3": "VALUE_3",
    "default": "NA"
}
dictionary_test_2 = {
    "A item": "abcABC",
    "B item": "defDEF",
    "C item": "ghiGHI",
    "default": "hmmm"
}
dictionary_test_3 = {
    "first_item" : "VALUE_1",
    "second_item" : "VALUE_2",
    "third_item" : "VALUE_3",
    "default" :"NA" 
}

test_string_1 = 'some text before {{item1}} & {{item2}}'
test_string_2 = '{{A item}} && {{ hi }} && {{C item}}'
test_string_3 = 'first item is- {{first_item}} & {{second_item}} and then last item is {{third_item}}'


class TestUtils(unittest.TestCase):
    def test_glue_it(self):

        test_result1 = glue_it(test_string_1, dictionary_test_1)
        test_result2 = glue_it(test_string_2, dictionary_test_2)
        test_result3 = glue_it(test_string_3, dictionary_test_3)
        self.assertEqual(test_result1, 'some text before ABC & DEF')
        self.assertEqual(test_result2, 'abcABC && hmmm && ghiGHI')
        self.assertEqual(test_result3, 'first item is- VALUE_1 & VALUE_2 and then last item is VALUE_3')


if __name__ == '__main__':
    unittest.main()


# python -m unittest tests.unit_tests
