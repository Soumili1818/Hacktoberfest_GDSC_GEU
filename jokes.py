# Library used - pyjokes 

## !pip install pyjokes

import pyjokes

lmao = pyjokes.get_joke(language="en", category="neutral")

"""
Languages supported
en	English
de	German
es	Spanish
it	Italian
gl	Galician
eu 	Basque
"""

print(lmao) 
