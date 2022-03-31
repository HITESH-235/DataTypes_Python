print( "HELLO WORLD" , "\n" )

# 1 // Numeric (Int, float, complex)

print("INTEGERS :")
a0 = 108
print( "a0 =" , a0 , "\n" , type(a0) ,"\n" , type(a0) is int , "\n" )
#---------------------------------------------------------------------------------
print("FLOAT :")
a1 = 3.14
print( "a1 =" , a1 , "\n" , type(a1) , "\n" , type(a1) is float )
a2 = 2.5e4      # 2.5 x 10^4
print( "a2 =" , a2 , "\n" , type(a2) , "\n" , type(a2) is float , "\n" )
# ---------------------------------------------------------------------------------
print("COMPLEX NUMBERS :")
a3 = -2 - 5j
# (-2) is real part & (-5) is the imaginary & j = square root of (-1)
print( "a3 =" , a3 , "\n" , type(a3) , "\n" , type(a3) is complex )
a4 = 4j
# Remember that only j should be used to represent
print( "a4 =" , a4 , "\n" , type(a4) , "\n" , type(a4) is complex , "\n" )
# ---------------------------------------------------------------------------------
# Operations of complex numbers
print( "-2-5j + 0 + 4j = " , a3 + a4 )                   #ADDITION
print( "-2 - 5j - ( 0 - 4j ) = " , a3 - a4 )             #SUBTRACTION
print( "( -2 - 5j ) x ( 0 - 4j ) = " , a3*a4 )           #MULTIPLICATION
print( "( -2 - 5j ) / ( 0 - 4j ) = " , a3/a4 , "\n" )  #DIVISION
# ---------------------------------------------------------------------------------
# Other methods of complex numbers
print( "Conjugate of a3 & a4 :" , a3.conjugate() , "&" , a4.conjugate() )
print( "1 // Absolute value of a3 & a4 :" , float( "%.2f" % abs(a3) ) , "&" , float( "%.2f" % abs(a4) ) )
# OR :
print( "2 // Absolute value of a3 and a4 :" , format( abs(a3) , ".2f" ) , format( abs(a4) , ".2f") , "\n" )
# ---------------------------------------------------------------------------------
# Conversion in different numeric types:
print( "%d(an int), in float & complex is" % (a0) , float(a0) , "&"  , complex(a0) , "\n" )
print( a0 )       # Still the same
print( "%.2f(a float), in int & complex is" % (a1) , int(a1) , "&"  , complex(a1) , "\n" )
print( a1 )
#Complex numbers can neither be represented in form of integers, nor in float
# ---------------------------------------------------------------------------------

# 2 // None (Contains no value or object)
a = None
print( "a =" , a , "\n" , type(a) , "\n" , a is None , "\n" )
# It is kind of exception in all types

