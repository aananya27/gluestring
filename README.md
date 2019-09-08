# GlueString String Manipulator Package


## Table of contents

-   [Install](#install)
-   [Usage](#usage)
-   [Options (Coming Soon) ](#options)

## Install

`pip3 install gluestring`


## Usage

```python
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


<!-- ## Recipes -->
