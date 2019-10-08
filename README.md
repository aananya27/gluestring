# GlueString

![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)
[![Language: python](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)&nbsp;


## About

Glustring allows you to work with string templates flawlessly. 
You can create multiple `Gluegun`'s and generate strings out your templates with just one function. 

List of template with one mapping, one template with a list of mapping or a list of templates with list of mappings, All possible with one type agnostic `glue_it` method !

Checkout the [Recipes](#recipes) to see how gluestring package in actions

## Table of contents

1.   [Install](#install)
2.   [Usage](#usage)
3.   [Recipes](#recipes)
        - [List of input strings with single dictionary](#list-of-input-strings-with-single-dictionary)
        - [Single input string with list of dictionary](#single-input-string-with-list-of-dictionary)
        - [List of input strings with list of dictionary](#list-of-input-strings-with-list-of-dictionary)



## Install

`pip3 install gluestring` 

## Usage

``` python
from gluestring import Gluegun

pet_gluegun = Gluegun({
            "pups": "🐶🐶🐶",
            "kittens": "🐱🐱🐱",
            "fishes": "🐠🐠🐠",
            "octopus": "🐙🐙🐙"
        })
result = pet_gluegun.glue_it(" I Love {{pups}} more than {{octopus}}.")
print(result) 
# I Love 🐶🐶🐶 more than 🐙🐙🐙.
```

## Recipes
####  List of input strings with single dictionary
``` python

name_gluegun = Gluegun({
        "name": "Fee",
        "age" : 27,
        "animal":"Kittens🐱"
})
result_list = name_gluegun.glue_it([
        "Hello my name is {{name}} and i'm {{age}}.",
        "{{name}} is good with {{animal}}!"
        ])

print(result_list[0])
print(result_list[1])

# 'Hello my name is Fee and i'm 27.'
# 'Fee is good with Kittens🐱!'
```

#### Single input string with list of dictionary
``` python

name_gluegun = Gluegun([{
        "name": "Fee",
        "animal":"Kittens🐱"
        },
        {
        "name": "Foo",
        "animal":"Puppers🐶"

        }])
result_list = name_gluegun.glue_it(
        "Hello my name is {{name}} and I love {{animal}}."
        )

print(result_list[0])
print(result_list[1])

# 'Hello my name is Fee and I love Kittens🐱.'
# 'Hello my name is Foo and I love Puppers🐶.'
```
#### List of input strings with list of dictionary
```python
name_gluegun = Gluegun([{
        "name": "Fee",
        "animal":"Kittens🐱"
        },
        {
        "name": "Foo",
        "age":14,
        "animal":"Puppers🐶"

        }])
result_list = name_gluegun.glue_it([
        "Hello my name is {{name}} and i'm {{age}}.",
        "{{name}} is good with {{animal}}!"
        ])
print(result_string_list[0])
print(result_string_list[1])
print(result_string_list[2])
print(result_string_list[3])
# 'Hello my name is Fee and i'm NA.'
# 'Hello my name is Foo and i'm 14.'
# 'Fee is good with Kittens🐱!'
# 'Foo is good with Puppers🐶!'
```
*  Will not throw exception on unknown keys, will use `NA`, you can override it by adding a `default` key in the dictionary.
``` python
offer_gluegun = Gluegun({
            "offer_thirty": "30%",
            "offer_fourty": "40%",
        })
result_string = offer_gluegun.glue_it(
        "Get {{alien_offer}} off & {{offer_fourty}} off if SUPER user."
        )
print(result_string)
# 'Get NA off & 40% off if SUPER user.
```
