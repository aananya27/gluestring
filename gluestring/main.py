import re

def glue_it(templateString, dictionaryToMatch):
    pattern = re.compile(r'\{\{([^}$]*)\}\}')
    number_of_patterns_found = len(pattern.findall(templateString))

    for i in range(number_of_patterns_found):
        val = pattern.search(templateString).groups()[0]

        if val.strip() in dictionaryToMatch:
            templateString = templateString.replace('{{'+val+'}}',dictionaryToMatch[val.strip()])
        else:
            templateString = templateString.replace('{{'+val+'}}',dictionaryToMatch['default'])         
    return templateString

