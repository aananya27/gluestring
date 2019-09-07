from gluestring.main import glue_it

DEFAULT_DICTIONARY = {
    "default": "NA"
}


class Gluegun:
    def __init__(self, mapping=DEFAULT_DICTIONARY):
        print(type(mapping) is dict)
        if (type(mapping) is dict):
            self.mapping = {**DEFAULT_DICTIONARY, **mapping}
        elif (type(mapping) is list):
            defaulted_mapping_list = []
            for dictionary in mapping:
                defaulted_mapping_list.append(
                    {**DEFAULT_DICTIONARY, **dictionary}.copy())
            self.mapping = defaulted_mapping_list
        else:
            raise Exception(
                'Excpected type of mapping to be a dictionary or a list of dictionary. Got type {}'.format(type(mapping)))

    def glue_it(self, templateString):
        return glue_it(templateString, self.mapping)
