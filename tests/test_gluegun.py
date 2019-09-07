import unittest
from gluestring.gluegun import Gluegun

offer_dictionary = {
    "offer_thirty": "30%",
    "offer_fourty": "40%",
    "default": "null"
}
test_offer_string = "Get {{offer_thirty}} off . Get {{offer_fourty}} if SUPER user. "


class TestGluegun(unittest.TestCase):
    def test_gluegun(self):
        g1 = Gluegun(offer_dictionary)
        result_string = g1.glue_it(test_offer_string)
        self.assertEqual(
            result_string, 'Get 30% off . Get 40% if SUPER user. ')

    def test_gluegun__with_no_parameters_should_not_throw_error(self):
        g1 = Gluegun()
        result_string = g1.glue_it(test_offer_string)
        self.assertEqual(
            result_string, 'Get NA off . Get NA if SUPER user. ')

    def test_gluegun__with_no_default(self):
        offer_dictionary_without_default = {
            "offer_thirty": "30%",
            "offer_fourty": "40%",
        }
        test_offer_string_with_unknown_keys = "Get {{offer_alien}} off . Get {{offer_alien2}} if SUPER user. "
        g1 = Gluegun(offer_dictionary_without_default)
        result_string = g1.glue_it(test_offer_string_with_unknown_keys)

        self.assertEqual(
            result_string, 'Get NA off . Get NA if SUPER user. ')

    def test_gluegun__with_invalid_type(self):
        with self.assertRaises(Exception):
            Gluegun(27)

    def test_gluegun__with_list_of_dictionary(self):
        dictionary_list = [
            {
                "A": "a",
                "B": "b"
            },
            {
                "AB": "ab",
                "CD": "cd"
            }
        ]
        sut = Gluegun(dictionary_list)

        for mapie in sut.mapping:
            self.assertTrue(
                "default" in mapie)

    # All 4 options
    def test_gluegun_glueit__string_listdictionary(self):
        in_string = "Hello my name is {{name}} and {{age}}"
        in_dictionary = [{
            "name": "Foo"
        }, {
            "name": "Boo",
            "age": 17
        }, {
            "age": 52
        }]
        sut = Gluegun(in_dictionary)
        result_string_list = sut.glue_it(in_string)
        print(result_string_list)
        self.assertEqual(
            result_string_list[0], 'Hello my name is Foo and NA')
        self.assertEqual(
            result_string_list[1], 'Hello my name is Boo and 17')
        self.assertEqual(
            result_string_list[2], 'Hello my name is NA and 52')

    def test_gluegun_glueit__liststring_dictionary(self):
        in_string = ["Hello my name is {{name}} and {{age}}","{{name}} is a good {{gender}}"]
        in_dictionary = {
            "name": "Foo",
            "gender":"woman"
        }
        sut = Gluegun(in_dictionary)
        result_string_list = sut.glue_it(in_string)

        self.assertEqual(len(result_string_list),2)
        self.assertEqual(
            result_string_list[0], 'Hello my name is Foo and NA')
        self.assertEqual(
            result_string_list[1], 'Foo is a good woman')




    def test_gluegun_glueit__liststring_listdictionary(self):
        in_string = ["Hello my name is {{name}} and {{age}}","{{name}} is a good {{gender}}"]
        in_dictionary = [{
            "name": "Foo",
            "gender":"woman"
        },{
            "age":14
        }]
        sut = Gluegun(in_dictionary)
        result_string_list = sut.glue_it(in_string)

        self.assertEqual(len(result_string_list),4)
        self.assertEqual(
            result_string_list[0], 'Hello my name is Foo and NA')
        self.assertEqual(
            result_string_list[1], 'Hello my name is NA and 14')
        self.assertEqual(
            result_string_list[2], 'Foo is a good woman')
        self.assertEqual(
            result_string_list[3], 'NA is a good NA')


    # def test_gluegun_glueit__liststring_listdictionary(self):


if __name__ == '__main__':
    unittest.main()

# python3 -m unittest tests.test_gluestring
