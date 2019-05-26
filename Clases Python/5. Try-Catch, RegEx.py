#Try catch

try:
  print(x)
except:
  print("An exception occurred")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")

#RegEx

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"world$"	
# *	Zero or more occurrences	"aix*"	
# +	One or more occurrences	"aix+"	
# {}	Exactly the specified number of occurrences	"al{2}"	
# |	Either or



# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"r"ain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain" r"ain\B"	
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# The findall() function returns a list containing all matches.
# Return an empty list if no match was found:
x = re.findall("ai", str)

# search, solo el primero
x = re.search("\s", str)
#x.span() returns a tuple containing the start-, and end positions of the match.
#       x.start() x.end()
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match


# separa en cadenas divididas por lo q le pasemos
x = re.split("\s", str)
#solo la primera vez q salga
x = re.split("\s", str, 1)

#substituye
x = re.sub("\s", "9", str)