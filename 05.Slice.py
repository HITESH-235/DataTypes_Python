import time

print( "\nHello World\n" )
start = time.time()

# slice can be applied to strings
string = "Welcome to Hitesh-235"
print( "Whole String :" , string )
print( "0th(1st) character from left :" , string[ 0 ] )
print( "3rd(4th) to 7th character :" , string[ 3 : 7 ] )
print( "11th(12th) to last character :" , string[ 11 : ] )
print( "0th(1st) to 7th character :"  , string[ : 7 ])
print( "\nwhole string with 2 jumps at once :" , string[ : : 2 ] ) #default 1
print( "0th(1st) to 7th character :" , string[ 0 : 7 : 2 ] )
print( "\nlast character :" , string[ -1 ] )
print( "5th last character :" , string[ -5 ] )
# ---------------------------------------------------------------------------------

end = time.time()
print( "\nTIME TAKEN (nanoseconds)  =" , (end - start)*10**9 , "\n" )