from gluestring.main import glue_it


class Gluegun:
    def __init__(self, dictionaryToMatch):
        self.dictionaryToMatch = dictionaryToMatch

    def glue_it(self,templateString):
        return glue_it(templateString,self.dictionaryToMatch)

