#Literal String Interpolation - “f-strings”
  
 #Python supports multiple ways to format text strings.
   #These include %-formatting [1], str.format() [2], and string.Template [3].
   # Each of these methods have their advantages, but in addition have disadvantages that make them cumbersome to use in practice. 
   # This PEP proposed to add a new string formatting mechanism: Literal String Interpolation. 
   # In this PEP, such strings will be referred to as “f-strings”, taken from the leading character used to denote such strings, and standing for “formatted strings”.
   
 # This PEP does not propose to remove or deprecate any of the existing string formatting mechanisms.
 # F-strings provide a way to embed expressions inside string literals, using a minimal syntax.
 #  It should be noted that an f-string is really an expression evaluated at run time, not a constant value. 
 # In Python source code, an f-string is a literal string, prefixed with ‘f’, which contains expressions inside braces. 
 # The expressions are replaced with their values. 

# Some examples are:
  
import datetime
 #name = 'Fred'
 #age = 50
 #anniversary = datetime.date(1991, 10, 12)
# f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'

#'My name is Fred, my age next year is 51, my anniversary is Saturday, October 12, 1991.'
 #f'He said his name is {name!r}.'
#"He said his name is 'Fred'."


#Dictionary 
# Dictionary in Python is a collection of keys values, used to store data values
# Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces.
# Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces.
# to access dictionary elements, you can use the familiar square brackets along with the key to obtain its value. Following is a simple example −

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#print "dict['Age']: ", dict['Age']



