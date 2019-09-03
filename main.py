import gluestring
input_string = 'some text before {{first_item}} & {{second_item}} and then last text {{third_item}}'
dictionaryToMatch = {
    "first_item" : "VALUE_1",
    "second_item" : "VALUE_2",
    "third_item" : "VALUE_3",
    "default" :"NA" 
}
print(gluestring.glue_it(input_string,dictionaryToMatch))