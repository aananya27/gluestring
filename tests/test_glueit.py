import unittest
from gluestring.main import glue_it


class TestGlueit(unittest.TestCase):
    def test_glue_it(self):

        string = 'first item is- {{first_item}} & {{second_item}} and then last item is {{third_item}}'

        dictToMerge = {"first_item": "VALUE_1",
                       "second_item": "VALUE_2",
                       "third_item": "VALUE_3",
                       "default": "NA"}

        result = glue_it(string, dictToMerge)

        self.assertEqual(
            result, 'first item is- VALUE_1 & VALUE_2 and then last item is VALUE_3')

    def test_glue_it_____with_edge_spaces(self):
        string = 'GlueIt {{ space_left}} @ {{space_right }} @ {{ space_both }}'

        dictToMerge = {"space_left": "left",
                       "space_right": "right",
                       "space_both": "both",
                       "default": "NA"}

        result = glue_it(string, dictToMerge)

        self.assertEqual(
            result, 'GlueIt left @ right @ both')


if __name__ == '__main__':
    unittest.main()


# python3 -m unittest tests.test_glueit
