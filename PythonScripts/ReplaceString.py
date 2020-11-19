# This script was created as a part of package DynamoCZ
# More at http://en.vaseksmolik.cz
#
# INPUT : IN[0] = input text
# OUTPUT : OUT = repaired text

import re

#Text, which you want to replace in input text
# in this example "red, brown, yellow" will be replaced to "red, orange, yellow"
DeletedTextFrom = 'brown'
NewText = 'orange'

outtext = re.sub(TextToBeReplaced,"",IN[0])
OUT = outtext
