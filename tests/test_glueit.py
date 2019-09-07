import unittest
from gluestring.main import resolve_string


class TestGlueit(unittest.TestCase):
    def test_resolve_string__with_different_keys(self):

        string = 'first item is- {{first_item}} & {{second_item}} and then last item is {{third_item}}'

        dictToMerge = {"first_item": "VALUE_1",
                       "second_item": "VALUE_2",
                       "third_item": "VALUE_3",
                       "default": "NA"}

        result = resolve_string(string, dictToMerge)

        self.assertEqual(
            result, 'first item is- VALUE_1 & VALUE_2 and then last item is VALUE_3')

    def test_resolve_string__with_spaces_at_edges(self):
        string = 'GlueIt {{ space_left}} @ {{space_right }} @ {{ space_both }}'

        dictToMerge = {"space_left": "left",
                       "space_right": "right",
                       "space_both": "both",
                       "default": "NA"}

        result = resolve_string(string, dictToMerge)

        self.assertEqual(
            result, 'GlueIt left @ right @ both')

    def test_resolve_string__with_multiple_occurences_of_same_key(self):

        string = '{{first_item}} & {{first_item}} & {{first_item}}'

        dictToMerge = {"first_item": "VALUE_1",
                       "second_item": "VALUE_2",
                       "third_item": "VALUE_3",
                       "default": "NA"}

        result = resolve_string(string, dictToMerge)

        self.assertEqual(
            result, 'VALUE_1 & VALUE_1 & VALUE_1')





if __name__ == '__main__':
    unittest.main()


# python3 -m unittest tests.test_glueit
