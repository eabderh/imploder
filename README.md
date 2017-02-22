
# Description

This is a python utility that is incredibly useful for developing scripts while
testing them with the python interactive interpreter. It allows for reloads of
imported modules and puts the methods of the module in the current frame. It is
very similar to `from module import *`.

### Usage

``` python
from imploder import implode
from test import test_function

test_function()

# change something in the test function
implode()

# run updated function
test_function()
```






