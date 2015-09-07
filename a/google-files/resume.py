#!/usr/bin/python

import string

# cipher
#   abcdefghijklmnopqrstuvwxyz
#   27182818284590452353602874

tt = string.maketrans("abcdefghijklmnopqrstuvwxyz:/.","27182818284590452353602874:/.")
url = "http://www.mkaz.com/about/reume.html"

print string.translate(url, tt)

