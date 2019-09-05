from gluestring.main import glue_it

DEFAULT_DICTIONARY = {
            "default" : "NA"
        }



class Gluegun:
    def __init__(self,dictionaryToMatch=DEFAULT_DICTIONARY):
        self.dictionaryToMatch = { **DEFAULT_DICTIONARY, **dictionaryToMatch }

    def glue_it(self,templateString):
        return glue_it(templateString,self.dictionaryToMatch)


