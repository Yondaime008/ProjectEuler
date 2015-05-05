import re

regex = re.compile("(?:([A-Z])[a-z])")

strdata = 'ABcDefGHIjk'

print(m.group(1))