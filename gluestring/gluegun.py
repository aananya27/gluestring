from gluestring.main import glue_it

default_dictionary = {
            "default" : "NA"
        }



class Gluegun:
    def __init__(self,dictionaryToMatch=default_dictionary):
        self.dictionaryToMatch = { **default_dictionary, **dictionaryToMatch }

    def glue_it(self,templateString):
        return glue_it(templateString,self.dictionaryToMatch)


