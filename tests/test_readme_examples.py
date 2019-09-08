import unittest
from gluestring.gluegun import Gluegun


class TestGlueit(unittest.TestCase):
    def test_basic(self):
        #     pup_string = "I Love {{pups}} more than {{octopus}}."
        #     animal_dictionary = {
        #         "pups" : "🐶🐶🐶",
        #         "kittens":"🐱🐱🐱",
        #         "fishes":"🐠🐠🐠",
        #         "octopus":"🐙🐙🐙"
        #     }
        #     pet_string = Gluegun(animal_dictionary)
        #     pet_string.glue_it(pup_string)

        #     pet_string = resolve_string(pup_string, animal_dictionary)

        pet_gluegun = Gluegun({
            "pups": "🐶🐶🐶",
            "kittens": "🐱🐱🐱",
            "fishes": "🐠🐠🐠",
            "octopus": "🐙🐙🐙"
        })

        result = pet_gluegun.glue_it("I Love {{pups}} more than {{octopus}}.")
        self.assertEqual(result, 'I Love 🐶🐶🐶 more than 🐙🐙🐙.')

# python3 -m unittest tests.test_readme_examples
