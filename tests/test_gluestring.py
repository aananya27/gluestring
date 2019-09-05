import unittest
from gluestring.gluegun import Gluegun

offer_dictionary = {
    "offer_thirty" : "30%",
    "offer_fourty" : "40%",
    "default" : "null"
}
test_offer_string = "Get {{offer_thirty}} off . Get {{offer_fourty}} if SUPER user. "


class TestUtils(unittest.TestCase):
    def test_gluegun(self):
        g1 =Gluegun(offer_dictionary)
        result_string = g1.glue_it(test_offer_string)
        self.assertEqual(result_string, 'Get 30% off . Get 40% if SUPER user. ')




if __name__ == '__main__':
    unittest.main()

# python -m unittest tests.unit_tests
