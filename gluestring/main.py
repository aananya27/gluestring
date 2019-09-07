import re


def resolve_string(templateString, dictionaryToMatch):
    pattern = re.compile(r'\{\{([^}$]*)\}\}')
    number_of_patterns_found = len(pattern.findall(templateString))

    for _ in range(number_of_patterns_found):
        val = pattern.search(templateString).groups()[0]

        if val.strip() in dictionaryToMatch:
            templateString = templateString.replace(
                '{{'+val+'}}', str(dictionaryToMatch[val.strip()]), 1)
        else:
            templateString = templateString.replace(
                '{{'+val+'}}', str(dictionaryToMatch['default']), 1)
    return templateString

# def resolve_list(templateStringList, dictionaryToMatch ):
#     for templateString in templateStringList:


def resolve_mxn(templateStringList, dictionaryToMatchList):
    result = []
    for templateString in templateStringList:
        for dictionaryToMatch in dictionaryToMatchList:
            result.append(resolve_string(templateString, dictionaryToMatch))
    return result
