import re

input_string = 'some text before {{first_item}} & {{second_item}} and then last text {{third_item}}'

dictionaryToMatch = {
    "first_item" : "VALUE_1",
    "second_item" : "VALUE_2",
    "third_item" : "VALUE_3",
    "default" :"NA" 
}

def glue_string(templateString, dictionaryToMatch):
    pattern = re.compile('\{\{([^}$]*)\}\}')
    number_of_patterns_found = len(pattern.findall(templateString))
     
    for i in range(number_of_patterns_found):
        val = pattern.search(templateString).groups()[0]
        if val in dictionaryToMatch:
            templateString = templateString.replace('{{'+val+'}}',dictionaryToMatch[val])
        else:
            templateString = templateString.replace('{{'+val+'}}',dictionaryToMatch['default'])
    print(templateString)

# finalcall
glue_string(input_string,dictionaryToMatch)
