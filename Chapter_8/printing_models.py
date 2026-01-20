import printing_functions
print(printing_functions.print_function())

from printing_functions import print_function
print(print_function())

from printing_functions import print_function as pf
print(pf())

import printing_functions as print_f
print(print_f.print_function())

from printing_functions import *
print(print_function())