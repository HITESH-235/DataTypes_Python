import time

print( "HELLO WORLD" , "\n" )
start = time.time()

x = 100
y = 120
print( "Is x(100), greater than y(120) ?? :"  , x>y )
print( "Is x(100), smaller than y(120) ?? :"  , x<y , "\n" )
# ---------------------------------------------------------------------------------

if( x>y ) :  
        print( "Yes, x is greater than y." )
else :
        print( "No, x is smaller than y." )
# ---------------------------------------------------------------------------------

x0 = 100>120
print( "100>120 ?? :" , x0)
y0 = 120>100
print( "120>100 ?? :" , y0 , "\n" )
# ---------------------------------------------------------------------------------

print( True + True )
print( True*True )
print( True + False )
print( False - True )
# ---------------------------------------------------------------------------------

end = time.time()
print( "\nTIME TAKEN (nanoseconds)  =" , (end - start)*10**9 , "\n" )