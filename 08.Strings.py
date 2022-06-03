from time import*

print( "\nHello World\n" )
start = time()

print( '''A 
MULTI 
LINE
STRING
.........''')

stringx = "ab_cd"
print( stringx[1] ) # try all slicing methods

# Looping :
for i in stringx :
        print(i)

print( "Length :" , len(stringx) )
print( "Checking :" , "a" in stringx )
print( "Checking_2 :" , "a" not in stringx )
print( "Stripping :" , stringx.strip() ) # it removes every space at start and end of the string and returns the string
print( "Splitting :" , stringx.split("_") ) # splits into from wherever the given character is present and returns the string
# you can concatenate them simply like adding
txt = "My phone number is \"Why do you want??\"" # using same quotes between a string itself
print(txt)
# ---------------------------------------------------------------------------------

end = time()
print( "\nTIME TAKEN  =" , end-start , "\n" )