# Module in Python
# A module is simply a Python file (.py) that contains functions, classes,
# or variables you can import and use in another script.

import module_two as mt

mt.greet("momin") # funtion defined in another .py file

from module_two import salaam

salaam("Yaseen") # No need to use module name